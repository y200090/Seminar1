#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100
#define U 10000
#define L -10000

int calcMax(int a[]) {
    int i, max;

    max = a[0];
    for (i = 0; i < N; i++) {
        if (max < a[i]) {

            printf("  >> 最大値が更新されました。%d -> %d\n", max, a[i]);
            max = a[i];
        }
    }

    return max;
}

int calcMin(int a[]) {
    int i, min;

    min = a[0];
    for (i = 0; i < N; i++) {
        if (min > a[i]) {

            printf("  >> 最小値が更新されました。%d -> %d\n", min, a[i]);
            min = a[i];
        }
    }

    return min;
}

int main(void) {
    int i, j, r, a[N], max, min;

    srand((unsigned)time(NULL));

    time_t start_time, end_time;
    clock_t start_clock, end_clock;

    // printf("対象となる整数は\n[");
    for (i =0; i < N; i++) {
        r = (rand() % (U - L + 1)) + L;
        a[i] = r;

        // printf("%d", a[i]);
        // if (i < N - 1) {
        //     printf(", ");
        // }
    }
    // printf("]\nの%d個です。\n\n", N);
    printf("調査対象となる整数は%d個です。\n\n", N);

    start_time = time(NULL);
    start_clock = clock();

    max = calcMax(a);
    printf("\n最大値は%dです。\n\n", max);

    end_time = time(NULL);
    end_clock = clock();

    printf("最大値を計算するのに実時間で%ldかかりました。\n", end_time - start_time);
    printf("最大値を計算するのにCPU時間で%fかかりました。\n", (double)(end_clock - start_clock) / CLOCKS_PER_SEC);

    start_time = time(NULL);
    start_clock = clock();

    min = calcMin(a);
    printf("\n最小値は%dです。\n", min);

    end_time = time(NULL);
    end_clock = clock();

    printf("最小値を計算するのに実時間で%ldsかかりました。\n", end_time - start_time);
    printf("最小値を計算するのにCPU時間で%fsかかりました。\n", (double)(end_clock - start_clock) / CLOCKS_PER_SEC);

    return 0;
}
