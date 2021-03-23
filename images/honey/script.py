

#template="<div class=\"mySlides\">\n\t<div class=\"numbertext\">" + n +" / 53</div>\n\t<img src=\"../images/honey/hp (" + n + ").jpg\" style=\"width:100%\">\n\t<div class=\"text\"></div>\n</div>"

for i in range(53):
    n = i + 1
    template="<div class=\"mySlides\">\n\t<div class=\"numbertext\">" + str(n) +" / 53</div>\n\t<img src=\"../images/honey/hp (" + str(n) + ").jpg\" style=\"width:100%\">\n\t<div class=\"text\"></div>\n</div>"

    print(template)