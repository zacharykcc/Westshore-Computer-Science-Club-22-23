//wildcat_team=ZacharyW

#include <stdio.h>

int main() {

  char op;
  double first, second;
  //printf("Enter an operator (+, -, *, /): ");
  scanf("%c", &op);
  
  scanf("%lf %lf", &first, &second);

    if(op == 'add'){
      printf("%.1lf",first + second);
    }
    else if(op == 'sub'){
      printf("%.1lf",first - second);
    }
    else if(op == 'mul'){
      printf("%.1lf",first * second);
    }
    else if(op == 'div'){
      printf("%.1lf",first / second);
    }
    else{
      printf("Invalid Usage");
    }
  
}

// END_OF_SOURCE