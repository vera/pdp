#include <check.h>
#include <stdlib.h>

#define main __real_main
#include "../../../global.c"
#undef main

START_TEST(test_function_f)
{
    ck_assert_int_eq(f(0,1), 2*0*0/1);
    ck_assert_int_eq(f(5,1), 2*5*5/1);
    ck_assert_int_eq(f(10,1), 2*10*10/1);
    ck_assert_int_eq(f(999,1), 2*999*999/1);
    ck_assert_int_eq(f(0,5), 2*0*0/5);
    ck_assert_int_eq(f(5,5), 2*5*5/5);
    ck_assert_int_eq(f(10,5), 2*10*10/5);
    ck_assert_int_eq(f(999,5), 2*999*999/5);
    ck_assert_int_eq(f(0,10), 2*0*0/10);
    ck_assert_int_eq(f(5,10), 2*5*5/10);
    ck_assert_int_eq(f(10,10), 2*10*10/10);
    ck_assert_int_eq(f(999,10), 2*999*999/10);
    ck_assert_int_eq(f(0,999), 2*0*0/999);
    ck_assert_int_eq(f(5,999), 2*5*5/999);
    ck_assert_int_eq(f(10,999), 2*10*10/999);
    ck_assert_int_eq(f(999,999), 2*999*999/999);
    ck_assert_int_eq(f(-0,1), 2*0*0/1);
    ck_assert_int_eq(f(-5,1), 2*5*5/1);
    ck_assert_int_eq(f(-10,1), 2*10*10/1);
    ck_assert_int_eq(f(-999,1), 2*999*999/1);
    ck_assert_int_eq(f(-0,5), 2*0*0/5);
    ck_assert_int_eq(f(-5,5), 2*5*5/5);
    ck_assert_int_eq(f(-10,5), 2*10*10/5);
    ck_assert_int_eq(f(-999,5), 2*999*999/5);
    ck_assert_int_eq(f(-0,10), 2*0*0/10);
    ck_assert_int_eq(f(-5,10), 2*5*5/10);
    ck_assert_int_eq(f(-10,10), 2*10*10/10);
    ck_assert_int_eq(f(-999,10), 2*999*999/10);
    ck_assert_int_eq(f(-0,999), 2*0*0/999);
    ck_assert_int_eq(f(-5,999), 2*5*5/999);
    ck_assert_int_eq(f(-10,999), 2*10*10/999);
    ck_assert_int_eq(f(-999,999), 2*999*999/999);
    ck_assert_int_eq(f(0,-1), -2*0*0/1);
    ck_assert_int_eq(f(5,-1), -2*5*5/1);
    ck_assert_int_eq(f(10,-1), -2*10*10/1);
    ck_assert_int_eq(f(999,-1), -2*999*999/1);
    ck_assert_int_eq(f(0,-5), -2*0*0/5);
    ck_assert_int_eq(f(5,-5), -2*5*5/5);
    ck_assert_int_eq(f(10,-5), -2*10*10/5);
    ck_assert_int_eq(f(999,-5), -2*999*999/5);
    ck_assert_int_eq(f(0,-10), -2*0*0/10);
    ck_assert_int_eq(f(5,-10), -2*5*5/10);
    ck_assert_int_eq(f(10,-10), -2*10*10/10);
    ck_assert_int_eq(f(999,-10), -2*999*999/10);
    ck_assert_int_eq(f(0,-999), -2*0*0/999);
    ck_assert_int_eq(f(5,-999), -2*5*5/999);
    ck_assert_int_eq(f(10,-999), -2*10*10/999);
    ck_assert_int_eq(f(999,-999), -2*999*999/999);
}
END_TEST

Suite * test_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("global.c");

    /* Core test case */
    tc_core = tcase_create("Core");

    tcase_add_test(tc_core, test_function_f);
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

