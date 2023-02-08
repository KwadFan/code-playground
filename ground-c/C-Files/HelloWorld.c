#include <stdio.h>


int main(){


    // Single line comment

    /*
    Multi
    line
    comment
    */
    printf("HelloWorld"); // Prints no new line after string
    printf("Hello World\n"); // Prints new line after string
    printf("This\tline\thas\ttabs!\n"); // Print line with tabs

    /*
        A backslach is used as escape sequence
    */

    printf("Show how to print special characters like Quotes \" \'");
    printf("What if I have to show a Backslash \\ ?"); // Print a backslash needs to be escaped..
    return 0;
}
