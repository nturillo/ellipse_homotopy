
libcomp:
	gcc -O3 -shared -o libcomp.so -fPIC computational_library.c -lgsl -lgslcblas -lm -Wall