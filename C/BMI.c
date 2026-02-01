#include <stdio.h>

int main() {

float Vægt = 0;
float Højde = 0;

// Input for vægt
printf("Indtast din vaegt i kilogram (kg): ");
scanf("%f", &Vægt);
// Input for højden
printf("Indtast din hoejde i meter (m): ");
scanf("%f", &Højde);

// BMI beregning
float BMI = Vægt / (Højde * Højde);

printf("Din BMI er: %.2f\n", BMI);

// Vægt grænser
if (BMI < 18.5) {
    printf("Du er undervaegtig\n");
}
else if (BMI >= 18.5 && BMI < 25) {
    printf("Du er normalvaegtig\n");
}
else {
    printf("Du er overvaegtig\n");
}
return 0;


printf("");

}
