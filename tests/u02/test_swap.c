#include <check.h>
#include <stdlib.h>

#define main __real_main
#include "../../../swap.c"
#undef main

START_TEST(test_swap_function)
{
    int x = 5;
    int y = 10;
    swap(&x, &y);
    ck_assert_msg(x == 10 && y == 5, "Nach Aufruf von swap mit Pointern auf x=5 und y=10 sollte gelten: x==10 && y==5");
    int x2 = 123;
    int y2 = 321;
    swap(&x2, &y2);
    ck_assert_msg(x2 == 321 && y2 == 123, "Nach Aufruf von swap mit Pointern auf x=123 und y=321 sollte gelten: x==321 && y==123");
}
END_TEST

Suite * test_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("swap.c");

    /* Core test case */
    tc_core = tcase_create("Core");

    tcase_add_test(tc_core, test_swap_function);
    suite_add_tcase(s, tc_core);

    return s;
}

 int main(void)
 {
    int number_failed;
    Suite *s;
    SRunner *sr;

    s = test_suite();
    sr = srunner_create(s);

    srunner_run_all(sr, CK_NORMAL);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
 }

