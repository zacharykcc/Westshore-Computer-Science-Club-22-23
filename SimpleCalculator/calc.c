// wildcat_team=ZacharyW
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Include string.h for string functions

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Invalid Usage\n");
        return 1;
    }

    double num1 = atof(argv[1]);
    double num2 = atof(argv[3]);
    char *operator = argv[2]; // Change to char* and remove [0] index

    double result;

    // Use strcmp to compare strings
    if (strcmp(operator, "add") == 0) {
        result = num1 + num2;
        printf("%.0lf\n", result);
    } else if (strcmp(operator, "sub") == 0) {
        result = num1 - num2;
        printf("%.0lf\n", result);
    } else if (strcmp(operator, "mul") == 0) {
        result = num1 * num2;
        printf("%.0lf\n", result);
    } else if (strcmp(operator, "div") == 0) {
        if (num2 == 0) {
            printf("Invalid Usage\n");
            return 1;
        }
        result = num1 / num2;
        printf("%.0lf\n", result);
    } else {
        printf("Invalid Usage\n");
        return 1;
    }

    return 0;
}

// END_OF_SOURCE