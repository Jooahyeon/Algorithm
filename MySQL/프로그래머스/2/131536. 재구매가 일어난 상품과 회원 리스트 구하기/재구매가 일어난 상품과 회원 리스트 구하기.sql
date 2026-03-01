-- 코드를 입력하세요
-- 1) ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하기
-- 2) 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 
-- 3) 결과는 회원 ID를 기준으로 오름차순 정렬, 
-- 4) 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬
SELECT
     USER_ID
    ,PRODUCT_ID
FROM ONLINE_SALE
-- 재구매한 상품을 어떻게 구하지? 
-- 한 회원이 같은 상품 id가 2개인 경우 출력하도록 하면 되나?
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;