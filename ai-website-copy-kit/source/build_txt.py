# -*- coding: utf-8 -*-
import os, textwrap
from prompts import CATEGORIES, CORE_SIX, expanded
import matter as M
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L=[]; bar='='*72
L+= [M.TITLE.upper(), M.SUBTITLE, 'PLAIN-TEXT PROMPT LIBRARY (clean copy-paste)', '', 
 'How to use: copy everything between the START and END lines of a prompt, paste it into your AI chat,',
 'and replace every [PLACEHOLDER IN CAPITALS] with your own details. Square brackets containing a colon,',
 'such as [NEEDS INFO: ...], are markers the AI writes back to you. See the PDF for the full guide, the brief,',
 'the worked example and the quality checklist.', '', 'Licence: for use on your own and your clients\' websites. Do not resell or redistribute.', '', bar,
 'THE CORE SIX (explained on the brief)', bar]
for k,d in CORE_SIX: L+= [k, textwrap.fill(d,72,initial_indent='   ',subsequent_indent='   '), '']
for c in CATEGORIES:
    L+=['',bar,f"{c['n']:02d}. {c['title'].upper()}",bar]
    for p in c['prompts']:
        L+=['',f"PROMPT {p['n']}: {p['title']}", f"Use it when: {p['use']}", 'Fill in:']
        for k,v in p['fill']: L.append(f'  {k} - {v}')
        L+=['',f"----- START PROMPT {p['n']} -----", expanded(p).replace('\u201c','"').replace('\u201d','"').replace('\u2019',"'"), f"----- END PROMPT {p['n']} -----", f"Tip: {p['tip']}",'']
out=os.path.join(ROOT,'dist','AI-Website-Copy-Kit-Prompt-Library.txt')
open(out,'w',encoding='utf-8').write('\n'.join(L)+'\n'); print('wrote',out)
