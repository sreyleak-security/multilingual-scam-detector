# multilingual-scam-detector

Pattern-based detector for crypto scams targeting non-English speakers — Khmer, Vietnamese, Lao and more.

Maintained by [Srey Leak](https://github.com/sreyleak-security) — security researcher & anti-scam educator, Long Beach CA.
Built from patterns seen at Chainalysis (forensics) and Coinbase (detection systems), and from real messages brought to my community workshops.

> Scammers exploit language barriers. This project closes them.
> > **If someone asks for your seed phrase, it's a scam. Period. Even if they speak your language.**
> >
> > ## What it does
> >
> > - `detector/url-checker.py` — flags lookalike domains (rn/m, 0/o, homoglyphs) and known scam URL patterns
> > - - `detector/email-analyzer.py` — flags classic phishing structures in emails
> >   - - `detector/translation-scam-detector.py` — flags machine-translated official-looking pages (scam sites auto-translate)
> >    
> >     - ## Language patterns
> >    
> >     - - `languages/khmer-patterns.json` — Khmer scam sentence patterns
> >       - - `languages/vietnamese-patterns.json`
> >         - - `languages/lao-patterns.json`
> >           - - `languages/chinese-patterns.json` (planned)
> >            
> >             - Patterns are sentence fragments scammers reuse: refund offers, support requests for seed phrases, guaranteed-profit promises.
> >            
> >             - ## Status
> >            
> >             - Early. Patterns grow with every workshop. PRs with new scam messages (anonymized!) are welcome.
> >
> > ## License
> >
> > MIT
> > 
