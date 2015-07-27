
int isPrime(int n, int *a, int al)
{
    int result = 0;
    int i = 0;
    
    for (i = 0; a[i] * a[i] < n + 1 && i < al; i++) {
        
        if (n % a[i] == 0) {    
            return 0;
        }
    }
    
    return 1;
}

int countPrimes(int n) {

    int *a =(int*) malloc(n*sizeof(n));
    int l = 1;
    int m = 0;
    int i = 0;

    if (n < 3) return 0;

    a[0] = 2;

    for (i = 3; i < n; i++) {
                
        m = isPrime(i, a, l);

        if (m == 1) {
            
            a[l] = i;
            l++;
        }
    }

    return l;
}