     #include<stdio.h>
     int main()
     {
	  	FILE *file = fopen("test.txt", "w");

       	if(file == NULL) {
      		printf("Cant open the file.\n");

            fputs("Hello, World!", file);
      }
      int fclose(FILE *file);


      	return 1;
      

     file = fopen("test.txt", "r");

     if(file == NULL) {
        printf("Cant open the file.\n");
        return 1;
      
      file = fopen("test.txt", "a");
      if (file == NULL) {
        printf("Cant open the file.\n");
        return 1;
        fputs("Vertex",file);






}

int fclose(FILE *file);

    }
    }