#include <stdio.h>
#include <stdlib.h>

int main (int argc, char* argv[]) {

    if (argc < 3) {
	      printf("Usage %s [in_file] [out_file] [key_vaule:0~255, optional]\n", argv[0]);
	      return 0;
    }

    int keyint = 0xa8;
    if (argc >= 4) {
        keyint = atoi(argv[3]);
    }

  
    char* ifn = argv[1];
    char* ofn = argv[2];

    FILE* ifp = fopen(ifn, "rb");
    FILE* ofp = fopen(ofn, "wb");

    int c;
    while ((c = fgetc(ifp)) != EOF) {
        fputc(c ^ keyint, ofp);
    }

    return 0;

}
