#include <stdio.h>
#include <stdlib.h>
#include <time.h> //for random number seed
//computer picks a random number and user has to guess it
int main()
{
    int randomNumber = 0;
    int guess = 0;
    int numberOfGuesses;
    time_t t;

    //initialize random number generator
    srand((unsigned) time(&t));

    //get the random number
    randomNumber = rand() % 21;

    //intro game to user
    printf("\nThis is a guessing game.");
    printf("\nI have chosen a number between 0 and 20 that you must guess");

    for(numberOfGuesses = 5; numberOfGuesses > 0; --numberOfGuesses)

    {
        printf("\nYou have %d tr%s left.",numberOfGuesses, numberOfGuesses == 1 ? "y"  : "ies");
        printf("\nEnter a guess:");
        scanf("%d",&guess);

        if(guess == randomNumber)
        {
            printf("\nCongratulations, you guessed it!");
            break;
        }
        else if(guess < 0 || guess > 20)     //checking invalid guess
            printf("\nI said the number was between 0 and 20");
        else if(randomNumber > guess)
            printf("\n Sorry %d is wrong. My number is greater than that.", guess);
        else if(randomNumber < guess)
            printf("\n Sorry %d is wrong. My number is less than that.", guess);

        }
        if(numberOfGuesses < 1)
            {
            printf("\nYou had five tries and failed. The number was %d.", randomNumber);
            }
    return 0;
}
