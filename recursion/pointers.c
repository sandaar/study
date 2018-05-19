#include <stdio.h>

int main(){
  int arr[] = {10, 20, 30, 40, 50, 60};
  int *ptr1 = arr;
  printf("arr %p\n", &arr);
  printf("p = %p\n", ptr1);
  printf("*p = %d\n", *ptr1);
  int *unitialized_ptr;
  printf("unitialized_ptr = %p\n", unitialized_ptr);
  if (unitialized_ptr == NULL)
  {
    printf("unitialized_ptr is NULL!\n");
  }
  int *null_ptr =  NULL;
  printf("null_ptr = %p\n", null_ptr);
}
