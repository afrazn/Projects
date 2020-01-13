#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define GAME 3
//THIS PROJECT CREATES A TIC TAC TOE GAME
/*checkForWin
drawBoard
markBoard
*/

void printBoard(char* ticTac[GAME][GAME]) {
    printf("\n\t\tTic Tac Toe");
    printf("\n   -------------------------------------");
    printf("\n     Player 1 (X)     -     Player 2 (O)");
    int row;
    int col;
    printf("\n");
    for(row = 0; row < GAME; row++)
    {
        printf("\n");
        printf("\t      |       |\n");
        for(col = 0; col < GAME; col++)
        {
             printf("\t  %s   ", ticTac[row][col]);
             if(col != 2)
                printf("|");
        }
        if(row != 2)
            printf("\n\t______|_______|_______");
    }
    printf("\n\t      |       |\n");
}

int checkForWin(char* ticTac[GAME][GAME]) {
    if(strcmp(ticTac[row][col], "X") == 0) {

    }
    return 0;
}

int main()
{
    char* ticTac[GAME][GAME] =
    {
        { "1", "2", "3" },
        { "4", "5", "6" },
        { "7", "8", "9" }
    };

    printBoard(ticTac);

    int tries = 0;
    while(tries < 9) {
        char pos[256];
        printf("\nPlayer 1 enter a pos: ");
        scanf("%s", &pos);
        system("cls");
        for(int row = 0; row < 3; row++)
            for(int col = 0; col < 3; col++)
                if(strcmp(ticTac[row][col], pos) == 0)
                    ticTac[row][col] = "X";
        printBoard(ticTac);
        strcpy(pos, "");
        printf("\nPlayer 2 enter a pos: ");
        scanf("%s", &pos);
        system("cls");
        for(int row = 0; row < 3; row++)
            for(int col = 0; col < 3; col++)
                if(strcmp(ticTac[row][col], pos) == 0)
                    ticTac[row][col] = "O";
        printBoard(ticTac);
        tries++;
    }

    return 0;
}
