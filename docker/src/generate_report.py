    import json
    data = json.load(open('trivy.json'))
    count = {'CRITICAL':0,'HIGH':0,'MEDIUM':0,'LOW':0}
    for r in data.get('Results',[]):
        for v in r.get('Vulnerabilities',[]):
            sev = v.get('Severity','UNKNOWN')
            if sev in count: count[sev] += 1
    html = f"""<h1>Docker CVE Report</h1>
    <ul><li>CRITICAL: {count['CRITICAL']}</li>
    <li>HIGH: {count['HIGH']}</li>
    <li>MEDIUM: {count['MEDIUM']}</li>
    <li>LOW: {count['LOW']}</li></ul>"""
    open('report.html','w').write(html)