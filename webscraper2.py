from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html >
<html lang = "en">

<body >
<!-- Google Tag Manager(noscript) - ->
<noscript >
	<iframe src = "https://www.googletagmanager.com/ns.html?id=GTM-NVFPDWB"
	        height = "0" width = "0" style = "display:none;visibility:hidden" > </iframe >
</noscript >
<!-- End Google Tag Manager(noscript) - ->
<header role = "banner" class = "navbar navbar-fixed-top navbar-static" >
	<div class = "container" >

		<div class = "navbar-header" >

			<a data-toggle = "collapse-side" data-target = ".side-collapse" data-target-2 = ".side-collapse-container" >
				<button type = "button" class = "navbar-toggle pull-right collapsed" data-toggle = "collapse"
				        data-target = "#navbar" data-target-2 = ".side-collapse-container" data-target-3 = ".side-collapse"
				        aria-expanded = "false" aria-controls = "navbar" >

					<span class = "sr-only" > Toggle navigation < /span >
					<span class = "icon-bar top-bar" > </span >
					<span class = "icon-bar middle-bar" > </span >
					<span class = "icon-bar bottom-bar" > </span >

				</button >
			</a >
			<div class = "navbar-brand" >
				<a href = "/" > <img src = "/img/logo_white.svg" alt = "Web Scraper" > </a >
			</div >
		</div >

		<div class = "side-collapse in" >
			<nav id = "navbar" role = "navigation" class = "navbar-collapse collapse" >
				<ul class = "nav navbar-nav navbar-right" >
					<li class = "hidden" >
						<a href = "#page-top" > </a >
					</li >

					<li >
						<a href = "/" class = "menuitm" >
							<p > Web Scraper < /p >
							<div class = "crta" > </div >
						</a >
					</li >
					<li >
						<a href = "/cloud-scraper" class = "menuitm" >
							<p > Cloud Scraper < /p >
							<div class = "crta" > </div >
						</a >
					</li >
					<li >
						<a href = "/pricing" class = "menuitm" >
							<p > Pricing < /p >
							<div class = "crta" > </div >
						</a >
					</li >

					<li class = "dropdown" >
						<a href = "#section3" class = "menuitm dropdown-toggle" data-toggle = "dropdown" >
							<p > Learn < /p >
							<div class = "crta" > </div >
						</a >
						<ul class = "dropdown-menu" >
							<li >
								<a href = "/documentation" > Documentation < /a >
							</li >
							<li >
								<a href = "/tutorials" > Video Tutorials < /a >
							</li >
							<li >
								<a href = "/test-sites" > Test Sites < /a >
							</li >
							<li >
								<a href = "https://forum.webscraper.io/" target = "_blank" rel = "noopener" > Forum < /a >
							</li >
						</ul >
					</li >
					<li >
						<a target = "_blank" href = "https://chrome.google.com/webstore/detail/web-scraper/jnhgnonknehpejjnehehllkliplmbmhn?hl=en" class = "btn-menu1 install-extension" rel = "noopener" > Install < /a >
					</li >
					<li >
						<a href = "https://cloud.webscraper.io/" class = "btn-menu2" > Login < /a >
					</li >
				</ul >
			</nav >
		</div >
	</div >
</header >

<div class = "wrapper" >
		<div class = "formenu-here container-fluid" >

	</div>
	<div class="container-fluid blog-hero">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<h1>Test Sites</h1>
				</div>
			</div>
		</div>
	</div>

	<div class="container test-site">
		<div class="row">
			<div class="col-md-3 sidebar">
					<div class="navbar-default sidebar" role="navigation">
	<div class="sidebar-nav navbar-collapse">
		<ul class="nav" id="side-menu">

			<li >
				<a href="/test-sites/e-commerce/allinone">Home</a>
			</li>

						<li class="active">
				<a href="/test-sites/e-commerce/allinone/computers" class="category-link active">
					Computers
					<span class="fa arrow"></span>
				</a>

								<ul class="nav nav-second-level collapse in">
										<li>
						<a href="/test-sites/e-commerce/allinone/computers/laptops" class="subcategory-link ">
							Laptops
						</a>
					</li>
										<li>
						<a href="/test-sites/e-commerce/allinone/computers/tablets" class="subcategory-link ">
							Tablets
						</a>
					</li>
									</ul>
							</li>
						<li >
				<a href="/test-sites/e-commerce/allinone/phones" class="category-link ">
					Phones
					<span class="fa arrow"></span>
				</a>

							</li>
					</ul>
	</div>
</div>

			</div>
			<div class="col-md-9">

	<h1 class="page-header">Computers category</h1>

	<h2>Top items being scraped right now</h2>

	<div class="row">
			<div class="col-sm-4 col-lg-4 col-md-4">
	<div class="thumbnail">
		<img class="img-responsive" alt="item"
		     src="/images/test-sites/e-commerce/items/cart2.png">
		<div class="caption">
			<h4 class="pull-right price">$410.46</h4>
			<h4>
									<a href="/test-sites/e-commerce/allinone/product/560" class="title" title="Acer Aspire ES1-732 Black">Acer Aspire ES1-...</a>
							</h4>
			<p class="description">Acer Aspire ES1-732 Black, 17.3&quot; HD+, Celeron, N3350, 4GB, 1TB, Windows 10 Home</p>

		</div>
		<div class="ratings">
			<p class="pull-right">14 reviews</p>
			<p data-rating="4">
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
							</p>
		</div>
	</div>
</div>
			<div class="col-sm-4 col-lg-4 col-md-4">
	<div class="thumbnail">
		<img class="img-responsive" alt="item"
		     src="/images/test-sites/e-commerce/items/cart2.png">
		<div class="caption">
			<h4 class="pull-right price">$488.64</h4>
			<h4>
									<a href="/test-sites/e-commerce/allinone/product/575" class="title" title="Acer Swift 1 SF113-31 Silver">Acer Swift 1 SF1...</a>
							</h4>
			<p class="description">Acer Swift 1 SF113-31 Silver, 13.3&quot; FHD, Pentium N4200, 4GB, 128GB SSD, Windows 10 Home</p>

		</div>
		<div class="ratings">
			<p class="pull-right">4 reviews</p>
			<p data-rating="3">
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
							</p>
		</div>
	</div>
</div>
			<div class="col-sm-4 col-lg-4 col-md-4">
	<div class="thumbnail">
		<img class="img-responsive" alt="item"
		     src="/images/test-sites/e-commerce/items/cart2.png">
		<div class="caption">
			<h4 class="pull-right price">$99.99</h4>
			<h4>
									<a href="/test-sites/e-commerce/allinone/product/512" class="title" title="Iconia B1-730HD">Iconia B1-730HD</a>
							</h4>
			<p class="description">Black, 7&quot;, 1.6GHz Dual-Core, 8GB, Android 4.4</p>

		</div>
		<div class="ratings">
			<p class="pull-right">1 reviews</p>
			<p data-rating="3">
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
								<span class="glyphicon glyphicon-star"></span>
							</p>
		</div>
	</div>
</div>
	</div>


			</div>
		</div>
	</div>
	<div class="clearfix"></div>
	<div class="push"></div>
</div>

<div class="container-fluid footer" id="layout-footer">
	<div class="container">
		<div class="row">
			<div class="col-md-3">
				<ul>
					<li><p>Products</p></li>
					<li>
						<a href="/">Web Scraper browser extension</a>
					</li>
					<li>
						<a href="/pricing">Web Scraper Cloud</a>
					</li>


				</ul>
			</div>
			<div class="col-md-3">
				<ul>
					<li><p>Company</p></li>

					<li><a href="/contact">Contact</a>
					</li>

					<li>
						<a href="/privacy-policy">Privacy Policy</a>
					</li>
					<li>
						<a href="http://webscraperio.us-east-1.elasticbeanstalk.com/downloads/Web_Scraper_Media_Kit.zip">Media kit</a>
					</li>

					<li><a href="/jobs">Jobs</a></li>
				</ul>
			</div>
			<div class="col-md-3">
				<ul>
					<li><p>Resources</p></li>
					<li><a href="/blog">Blog</a></li>
					<li>
						<a href="/documentation">Documentation</a>
					</li>
					<li>
						<a href="/tutorials">Video Tutorials</a>
					</li>
					<li>
						<a href="/screenshots">Screenshots</a>
					</li>
					<li>
						<a href="/test-sites">Test Sites</a>
					</li>
					<li>
						<a target="_blank" href="https://forum.webscraper.io/" rel="noopener">Forum</a>
					</li>
				</ul>
			</div>
			<div class="col-md-3">
				<ul>
					<li><p>CONTACT US</p></li>
					<li>
						<a href="mailto:info@webscraper.io">info@webscraper.io</a>
					</li>

					<li>Sporta street 2,<br> Riga, Latvia, LV-1013</li>
				</ul>
				<ul class="smedia">
					<li>
						<a href="https://www.facebook.com/webscraperio/" target="_blank" rel="noopener"><img src="/img/fbicon.png" alt="Web Scraper on Facebook"></a>
					</li>
					<li>
						<a href="https://twitter.com/webscraperio" target="_blank" rel="noopener"><img src="/img/twicon.png" alt="Web Scraper on Twitter"></a>
					</li>


				</ul>
			</div>
		</div>
		<div class="row">
			<div class="col-md-12">
				<p class="copyright">Copyright &copy 2020
					<a href="#">Web Scraper</a> | All rights
					reserved | Made by zoom59</p>
			</div>
		</div>
	</div>
</div>


</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')


# el = soup.find('div')
# el = soup.find_all('div')
# el = soup.find(id="section-1")
# el = soup.find(class_='crta')
# el = soup.select('.crta')

# el = soup.find(class_='dropdown-menu').get_text()

for item in soup.select('.title'):
    print(item.get_text())

print(el)
2wwww