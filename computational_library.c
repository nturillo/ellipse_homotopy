#include <stdbool.h>
#include <math.h>
#include <stdio.h>

#include <gsl/gsl_poly.h>

void find_d_distance_point_on_ellipse(double d, double x_0, double y_0, double a, double result[2]) {
    // give a point p_0 = (x_0, y_0) on an ellipse described by x^2/a^2 + y^2 = 1, find the point p_1 on the ellipse that is d Euclidean distance away from p_0 in the counter-clockwise direction
    // d = distance of interest
    // x_0 = x-coordinate of point on ellipse
    // y_0 = y-coordinate of point on ellipse
    // a = semi-major axis of ellipse

    if (a > sqrt(2)) {
        printf("Warning: find_d_distance_point_on_ellipse not tested for a > sqrt(2)\n");
    }

    // the farthest possible point on the ellipse is (-x_0, -y_0) (if a <= sqrt(2))
    // so, if d is greater than or equal to the chord length between p_0 and (-x_0, -y_0), then the point is just (-x_0, -y_0)
    if (a <= sqrt(2) && d >= 2*sqrt(pow(x_0, 2) + pow(y_0, 2))) {
        result[0] = -x_0;
        result[1] = -y_0;
        return;
    }

    // first, convert point to 1st quadrant
    int og_quad = 1;
    if (x_0 < 0) {
        x_0 = -x_0;
        if (y_0 < 0) {
            y_0 = -y_0;
            og_quad = 3;
        } else {
            og_quad = 2;
        }
    } else if (y_0 < 0) {
        y_0 = -y_0;
        og_quad = 4;
    }

    // solve system of equations
    // x^2/a^2 + y^2 = 1
    // (x - x_0)^2 + (y - y_0)^2 = d^2
    // using the parameterization
    // x = x_0 + (d)(1 - t^2)/(1+t^2)
    // y = y_0 + (d)(2t)/(1+t^2)
    // acquire the following quartic
    // t^4((-2x_0d + d^2)/(a^2)) + t^3(4y_0d) + t^2(4d^2 - 2d^2/a^2) + t(4y_0d) + (2x_0d + d^2)/(a^2) = 0
    // At^4 + Bt^3 + Ct^2 + Dt + E = 0

    double A = (-2*x_0*d + pow(d, 2))/(pow(a, 2));
    double B = 4*y_0*d;
    double C = 4*d*d - 2*pow(d, 2)/pow(a, 2);
    double D = 4*y_0*d;
    double E = (2*x_0*d + pow(d, 2))/(pow(a, 2));

    const double coeffs[5] = {E, D, C, B, A};
    double roots[8];
    gsl_poly_complex_workspace *w = gsl_poly_complex_workspace_alloc(5);
    gsl_poly_complex_solve(coeffs, 5, w, roots);
    gsl_poly_complex_workspace_free(w);
    //print roots
    for (int i = 0; i < 4; i++) {
        //printf("Root %d: %lf + %lfi\n", i + 1, roots[2*i], roots[2*i + 1]);
    }

    // find the real roots
    double real_roots[2];
    int num_real_roots = 0;
    for (int i = 0; i < 4; i++) {
        if (fabs(roots[2*i + 1]) < 1e-10) {
            real_roots[num_real_roots++] = roots[2*i];
        }
    }

    // if there are no real roots, or if there is one real root of multiplicity two:
    // the circle is bigger than the entire ellipse, meaning the d_distance point is just the furthest point on the ellipse
    // this should have already been caught at the beginning of the function, though
    //printf("x_0: %lf\n", x_0);
    //printf("y_0: %lf\n", y_0);
    //printf("Num Real Roots: %d\n", num_real_roots);
    //printf("Real Roots: %lf, %lf\n", real_roots[0], real_roots[1]);
    if (num_real_roots == 0 || (fabs(real_roots[0] - real_roots[1]) < 1e-6)) {
        printf("Warning: only 0 or 1 real roots found\n");
        if (og_quad == 1) {
            result[0] = -x_0;
            result[1] = -y_0;
        } else if (og_quad == 2) {
            result[0] = -x_0;
            result[1] = y_0;
        } else if (og_quad == 3) {
            result[0] = x_0;
            result[1] = y_0;
        } else {
            result[0] = x_0;
            result[1] = -y_0;
        }
        return;
    }

    // find the corresponding x and y values
    double x_1, y_1, x_2, y_2;
    double t_1 = real_roots[0];
    double t_2 = real_roots[1];
    x_1 = x_0 + d*(1 - pow(t_1, 2))/(1 + pow(t_1, 2));
    y_1 = y_0 + d*2*t_1/(1 + pow(t_1, 2));
    x_2 = x_0 + d*(1 - pow(t_2, 2))/(1 + pow(t_2, 2));
    y_2 = y_0 + d*2*t_2/(1 + pow(t_2, 2));

    // find the counter-clockwise point in the reference of quadrant one
    int ccw = 1;
    if (fabs(y_2 - y_1) < 1e-10) { // if p_0 is at the very top of the ellipse, the y-values will be the same. In this case, the left one is the closest counterclockwise 
        if (x_1 < x_2) {
            ccw = 1;
        } else {
            ccw = 2;
        }
    } else
    if (y_1 < y_2) { 
        ccw = 2;
    }
    
    // find the counter-clockwise point based off of the original quadrant
    double x_ccw, y_ccw;
    if (og_quad == 1) {
        if (ccw == 1) {
            x_ccw = x_1;
            y_ccw = y_1;
        } else {
            x_ccw = x_2;
            y_ccw = y_2;
        }
    } else if (og_quad == 2) {
        if (ccw == 1) {
            x_ccw = -x_2;
            y_ccw = y_2;
        } else {
            x_ccw = -x_1;
            y_ccw = y_1;
        }
    } else if (og_quad == 3) {
        if (ccw == 1) {
            x_ccw = -x_1;
            y_ccw = -y_1;
        } else {
            x_ccw = -x_2;
            y_ccw = -y_2;
        }
    } else {
        if (ccw == 1) {
            x_ccw = x_2;
            y_ccw = -y_2;
        } else {
            x_ccw = x_1;
            y_ccw = -y_1;
        }
    }

    result[0] = x_ccw;
    result[1] = y_ccw;
}

int num_loops(double d, double x_0, double y_0, double a, int num_steps) {
    // given a point p_0 = (x_0, y_0) on an ellipse described by x^2/a^2 + y^2 = 1, AND in the first quadrant, find the number of loops that the point will make around the ellipse if it takes num_steps many steps of d Euclidean distance in the counter-clockwise direction
    // d = distance of interest
    // x_0 = x-coordinate of point on ellipse
    // y_0 = y-coordinate of point on ellipse
    // a = semi-major axis of ellipse
    // num_steps = number of steps to take

    if (x_0 < 0 || y_0 < 0) {
        printf("Point must be in the first quadrant\n");
        return -1;
    }

    double curr_point[2] = {x_0, y_0};
    double prev_point[2];

    bool neg_to_pos = false; // true if the current point has positive y-value and the previous point had negative y-value
    int num_loops = 0;

    for (int step = 0; step < num_steps; step++) {
        prev_point[0] = curr_point[0];
        prev_point[1] = curr_point[1];

        find_d_distance_point_on_ellipse(d, prev_point[0], prev_point[1], a, curr_point);

        if (!neg_to_pos && prev_point[1] < 0 && curr_point[1] > 0) {
            neg_to_pos = true;
        }
        if (neg_to_pos && (x_0 - curr_point[0] > -1e-8)) {
            num_loops++;
            neg_to_pos = false;
        }
        //printf("Step %d: (%lf, %lf)\n", step + 1, curr_point[0], curr_point[1]);
        //printf("Neg to Pos: %d\n", neg_to_pos);
        //printf("Num Loops: %d\n", num_loops);
    }

    return num_loops;
}

int max_loops(double d, int n, double x_0[], double y_0[], double max_point[2], double a, int num_steps, int stop_early) {
    // find the maximum number of loops made over all points in the list
    // see num_loops(double d, double x_0, double y_0, double a, int num_steps) for parameter descriptions
    // max_point = the point that makes the most loops
    // stop_early = if not 0, stop early after finding a point that makes stop_early loops

    int max_loops = 0;
    max_point[0] = -1;
    max_point[1] = -1;
    for (int i = 0; i < n; i++) {
        int loops = num_loops(d, x_0[i], y_0[i], a, num_steps);
        if (loops > max_loops) {
            max_loops = loops;
            max_point[0] = x_0[i];
            max_point[1] = y_0[i];
            if (stop_early && loops >= stop_early) {
                return max_loops;
            }
        }
    }
    return max_loops;
}
