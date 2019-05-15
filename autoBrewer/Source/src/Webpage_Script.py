f = open('BrewCrew2.html', 'r')
buul = 0
found = 0
buttons = True
html_table = []
for line in f:
	html_table.append(line)
f.close()
for i in range(0,len(html_table)):
	if "<th>" in html_table[i] and found == 0:
		html_table[i] = "<th>Type</th>"
		html_table[i+1] = "<th>Time</th>"
		html_table[i+2] = "<th>Style</th>"
		found = 1
		#print(i,i+1,i+2)
	if "<td>" in html_table[i]:
		html_table[i] = "<td>BEER stuff</td>"
	if "<!-- end of buttons-->" in html_table[i]:
		buttons = False
	if "<input" in html_table[i] and buttons:
		html_table[i] = "<input type='radio' id='OG Doom' name='Beer' value='Og Doom' checked />"
		html_table[i+1] = "<label for='OG Doom'>OG Doom</label>"
print(html_table)
f2 = open('BrewCrew3.html','w')

for i in range(0,len(html_table)):
	f2.write(html_table[i])
f2.close()