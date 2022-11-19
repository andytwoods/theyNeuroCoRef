import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
# note need to install above seperately
# python -m spacy download en
html = (open("aliceInWonderland/4560944924381563385_11-h-2.htm.xhtml", "r", encoding='utf-8')).read()
html2 = '''
<p>
Just then her head struck against the roof of the hall: in fact she was now
more than nine feet high, and she at once took up the little golden key and
hurried off to the garden door.
</p>
<p>
Poor Alice! It was as much as she could do, lying down on one side, to look
through into the garden with one eye; but to get through was more hopeless than
ever: she sat down and began to cry again.
</p>
<p>
“You ought to be ashamed of yourself,” said Alice, “a great
girl like you,” (she might well say this), “to go on crying in this
way! Stop this moment, I tell you!” But she went on all the same,
shedding gallons of tears, until there was a large pool all round her, about
four inches deep and reaching half down the hall.
</p>
<p>
After a time she heard a little pattering of feet in the distance, and she
hastily dried her eyes to see what was coming. It was the White Rabbit
returning, splendidly dressed, with a pair of white kid gloves in one hand and
a large fan in the other: he came trotting along in a great hurry, muttering to
himself as he came, “Oh! the Duchess, the Duchess! Oh! won’t she be
savage if I’ve kept her waiting!” Alice felt so desperate that she
was ready to ask help of any one; so, when the Rabbit came near her, she began,
in a low, timid voice, “If you please, sir—” The Rabbit
started violently, dropped the white kid gloves and the fan, and skurried away
into the darkness as hard as he could go.
</p>
'''


neuralcoref.add_to_pipe(nlp)
doc1 = nlp('My sister has a dog. She loves him.')
print(doc1._.coref_clusters)

doc2 = nlp(html)
for ent in doc2.ents:
    print(ent._.coref_cluster)