#include <stdio.h>
#include<time.h>

int countdown(int c){
    int count = c ;
    clock_t t;
    t= clock();
    while (count<=0)
    {   
        count+=-1;
    }
    t=clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC ;
    printf("This took %f seconds to compile in C \n ",time_taken);
    return time_taken;
 
}
