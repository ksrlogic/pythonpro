def tagParse(tag):
    p = tag.replace('<div class="cols">', "")
    t = p.replace('<div class="cols" style="width: 86px;">', "")
    j = t.replace('<div class="cols" style="width: 87px;">', "")
    last = j.replace('<ul', '</div>')
    result = last.split('</div>')
    return result