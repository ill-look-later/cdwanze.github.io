/* put $100 in all checking/savings accounts on date account opened */
insert  into transaction (txn_id, txn_date, account_id, txn_type_cd,
  amount, funds_avail_date)
select null, a.open_date, a.account_id, 'CDT', 100, a.open_date
from account a
where a.product_cd IN ('CHK','SAV','CD','MM');
