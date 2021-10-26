import itertools


MAX_PRICE = 30

main_courses_iter = zip(main_courses, price_main_courses)
desserts_iter = zip(desserts, price_desserts)
drinks_iter = zip(drinks, price_drinks)
for (mc, mc_p), (dst, dst_p), (drnk, drnk_p) in itertools.product(main_courses_iter, desserts_iter, drinks_iter):
    total_price = mc_p + dst_p + drnk_p
    if total_price <= MAX_PRICE:
        print(mc, dst, drnk, total_price)
