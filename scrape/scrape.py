import twint

c = twint.Config()
c.Search = "Trump"
c.Limit = 1000
c.Store_csv = True
c.Output = "trump.csv"

twint.run.Search(c)
