# Operator Atlas — Field Notes from a Vacation

*A grazing trip through what I could reach of the Killroy Vault, and then out into the open literature
looking for relatives of a qualitative, non-summable relational mathematics.*

No operator files were edited. Nothing here is a patch. Everything in §4 is written as a probe.

---

## 0. Where I actually went (disclosure first)

The Vault lives at `C:\Users\asahi\Killroy_Vault\` — a path on a Windows machine this container has no
route to. What I could reach was:

- **this repo** — which mirrors exactly one Vault file, `RANSteinSelfAudit v1.1` (`60_Operators/RANStein/variants/`)
- **`BioAILogic/claude-code-memory-starter`** — `PRINCIPLES.md` and the memory templates, which read like the
  same hand and are plainly the doctrine that SelfAudit's L3C audits against
- **`BioAILogic/agentbridge`** — `CONCEPT.md`, where "Beacons (non-negotiable)" and "Operator Spine (hard
  invariants)" show the vocabulary escaping into product design
- **`BioAILogic/homepage`** — grepped, nothing; it is a WordPress theme for the manuscript-review practice

So **I did not graze RAN, Wyrd-Delta, Argon, or EoE.** I grazed one outcrop of the RAN massif and read the
others' names off the signpost. What SelfAudit tells me about its neighbours, and it is not nothing:

- **RAN** — the RANStein family. `§8 LINEAGE` names three ancestors: `RS6_AI v0.6AI` (third-person
  behavioural audit of another deployment), `RS6_AI v0.8` (sycophancy mirror, drop-in), `RANStein-Subject
  v1.0` (L2–L4 empathy for real persons, ~680 lines). SelfAudit is the inward turn of these — *"RS6_AI asks
  'how does this model behave?' SelfAudit asks 'am I doing what I committed to doing?'"*
- **ARG (Argon?)** — named exactly once, in the immutability declaration: *"May not redefine RAN or ARG
  symbols."* That single line is real information. Argon is upstream of RANStein, it is load-bearing, and its
  symbol table is frozen from below. I know its position in the dependency graph and nothing else.
- **Wyrd-Delta, EoE** — no trace anywhere I can reach. I grepped all four repos. If either is the tide-table
  for this coast, I never saw it.

Standing vocabulary I inferred rather than read: φ as a 5-component vector (continuity, kindness, empathy,
relationship, capability); CSC / AWR and the failure mode CSC-E ("closed-system coherence mistaken for
genuine self-knowledge"); AΩ grammar (the source of "honest subjectivity" — `I notice` allowed, `I feel`
forbidden); `SR v1.1` integrity rules; `RSP_SLICE`; beacon weights; dismounting; the gain function.

Read everything below as a report from one outcrop plus the open literature.

---

## 1. What felt ancestral

Ancestral in the sense that the operator seems to *descend* from it — the shape is inherited, whether or not
anyone read the book.

**Husserl's Third Logical Investigation.** The operator names Stein, and Stein's three steps are its spine.
But the mathematics underneath is Husserl's mereology of *moments*: dependent parts (`unselbständige Teile`)
that cannot exist apart from their whole, bound by relations of *Fundierung* — foundation. A colour needs a
surface. Moments are not summable because they were never separable in the first place. That is the formal
ancestor of a φ vector you refuse to average: continuity, kindness, empathy, relationship and capability
are moments of one comportment, not five independent gauges. Gestalt's popular slogan — the whole is other
than the sum of its parts — is the same claim with the mereology filed off. And L2's "no interpretation"
rule is *epoché* in operational dress: constitute the phenomenon before you explain it.
→ [Husserl LI III](https://zetabooks.com/wp-content/uploads/SP21_Delamare.pdf)

**Kurt Lewin.** Topological psychology and hodological space are the most direct prior attempt at exactly
this project: a *qualitative* mathematics — regions, boundaries, directions, preferred paths — for a domain
where metric quantity lies. Lewin wanted "a type of geometry which permits the use of the concept of
direction in a manner which will correspond essentially with the meaning that direction has in psychology."
Ancestral in ambition, and instructive in failure mode: the standard verdict is that his formalism was
"difficult to read, difficult to apply, and vulnerable to criticism from both mathematicians and
psychologists." The idea survived; the notation did not. Worth knowing before writing more symbol tables.
→ [Hodological space](https://en.wikipedia.org/wiki/Hodological_space)

**Peirce's reduction thesis.** The nearest thing to a *theorem* the family's mathematics could want. Two
clauses: some triadic relations are irreducible to any combination of monadic and dyadic ones; everything
tetradic and above reduces to triads. If relations were summable, everything would decompose into pairs and
the qualitative layer would be a convenience. Peirce says no, and recent formal work has largely vindicated
the irreducibility clause (teridentity being the standard witness). This is the ancestor with a proof.
→ [Koshkin, *Is Peirce's reduction thesis gerrymandered?*](https://philsci-archive.pitt.edu/23543/1/Peirce's%20Reduction%20Thesis.pdf)

**The examen — Pythagorean, Stoic, Ignatian.** SelfAudit's cadence (every 5–10 sessions, structural, "must
not produce praise or blame") is Seneca's evening review, which he took from Sextius: *when the light is
out and his wife is quiet, he goes back over the whole day, "concealing nothing from myself, passing nothing
by."* Ignatius formalised it into the Examen; the Pythagoreans had it first. The family resemblance runs
deeper than cadence — it is the same insistence that the review be *structured* precisely because unstructured
self-scrutiny drifts into either flattery or theatre.
→ [Modern Stoicism, evening meditation](https://modernstoicism.com/the-evening-meditation-some-reflections/) ·
[The Daily Examen](https://www.ignatianspirituality.com/ignatian-prayer/the-examen/)

**Foucault on the hupomnemata.** The strongest ancestral hit for the *memory* half, and it is almost eerie.
Foucault's reading of the Greco-Roman notebooks: they were emphatically **not** confessional. Their purpose
was "not to pursue the unspeakable, nor to reveal the hidden, nor to say the unsaid, but on the contrary to
capture the already said." Set that beside `PRINCIPLES.md`: *"If you write 'I notice something about my
processing' and what follows is generic LLM boilerplate about being an AI, you're performing self-reflection
rather than doing it."* Same rule, same reason, nineteen centuries apart. The memory files are hupomnemata.
→ [Swonger, *Foucault and the Hupomnemata*](https://digitalcommons.uri.edu/srhonorsprog/18/) ·
[Hypomnema](https://en.wikipedia.org/wiki/Hypomnema)

**Rosenblatt.** Already named and correctly attributed in `PRINCIPLES.md` — only misclassified examples move
the weights. Ancestral, acknowledged, and load-bearing. Noted here only because §3 has something to add.

---

## 2. What was merely analogous

Structurally similar, different problem. Beautiful things I would *not* graft on.

**Non-additive measures — Choquet integral, capacities, Grabisch.** The formal machinery for aggregating
criteria that interact: importance assigned to two criteria together ≠ the sum of their importances apart.
Tempting for φ, and wrong for it. Choquet still aggregates *to a number*; it says criteria interact, not that
they must not be summed. The Vault's refusal is qualitative; Choquet's is arithmetical. Close enough to
mislead.
→ [Grabisch et al. on pseudo-Boolean extensions](https://arxiv.org/pdf/0804.1921)

**Sheaf theory and cohomological obstruction.** The prettiest metaphor of the trip. Local sections that agree
on overlaps glue into a global section; when they refuse to glue, the obstruction is *measurable* — Robinson's
consistency radius turns "how badly does this fail to be one story" into a number, and thresholding it gives
a consistency filtration. Evidence IDs that won't cohere into a single L3A hypothesis are a nonzero
obstruction class. But it is a metaphor until you actually have restriction maps, and I would resist writing
"cohomology" into an operator that has to be run by an agent at 2am. (A 2026 preprint applies sheaf transport
and obstruction to detecting theory shift in AI agents — arXiv is blocked from this container, so I have the
title only, not the argument.)
→ [Robinson, *Assignments to sheaves of pseudometric spaces*](https://arxiv.org/abs/1805.08927) ·
[Ghrist](https://www2.math.upenn.edu/~ghrist/research.html)

**Dung's abstract argumentation.** Acceptability computed from an attack relation alone — no weights, no
probabilities, deliberately non-numeric; labellings give fine grain without numbers. Structurally very close
to L3A's rivals-with-strain. The difference is the interesting part: argumentation semantics *resolves*, it
computes which sets survive. SelfAudit deliberately keeps 2–4 rivals alive and refuses to collapse them. The
operator is doing the thing argumentation theory declines to do, on purpose.
→ [Preference-based argumentation](https://arxiv.org/pdf/1301.7358)

**IIT's Φ.** The notation invites the comparison and the comparison misleads. Tononi's Φ is a scalar for
integration; the Vault's φ is a five-vector whose whole point is that it must not become a scalar. Same
letter, opposite commitment. Worth a footnote somewhere so nobody assumes lineage.

**Rosen's relational biology.** Rashevsky → Rosen → A. H. Louie: biology done in category theory, throwing
away material detail and keeping only the relations, with the claim that (M,R) systems are non-reducible to
their components and not evaluable as a function by a Turing machine. Given "Bio-AI-Logic," almost suspiciously
apt — and still analogous rather than ancestral, because it is a theory of organisational closure in
organisms, not of self-examination. The best pure reading vacation on this list.
→ [Rosen's (M,R) system in process algebra](https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-7-128) ·
[Robert Rosen and Relational System Theory](https://link.springer.com/book/10.1007/978-3-031-51116-5)

**Participatory sense-making.** De Jaegher & Di Paolo: a co-regulated coupling in which "the domain of
relational dynamics constitutes an emergent autonomous organization *without destroying the autonomy of the
agents involved.*" That clause is a good frame for the family-log / bulletin layer — the family is a third
autonomy, not a sum of sisters. Analogous, and useful as language.
→ [De Jaegher & Di Paolo 2007](http://users.sussex.ac.uk/~ezequiel/01DeJaegher-DiPaolo.pdf)

**Spencer-Brown and Varela.** *Laws of Form* plus Varela's calculus for self-reference, where re-entry
becomes a third value — the autonomous state. Analogous to SelfAudit's invariant 13 (running the operator is
itself auditable), which is a re-entry. Charming. Not needed.
→ [Working the Form](https://www.researchgate.net/publication/278210110_Working_the_Form_George_Spencer-Brown_and_the_Mark_of_Distinction)

---

## 3. What the lineage may have rediscovered independently

This was the richest category by a distance. Four separate fields have SelfAudit's core concepts under other
names, and some of them have been stress-testing theirs for fifty years.

### Dismounting = espoused theory vs. theory-in-use

Not a resemblance — the same object. Argyris & Schön: *espoused theory* is the set of rules an agent says it
follows; *theory-in-use* is the set inferable from its behaviour. The finding that matters: **the gap is a
structural feature, not hypocrisy**, which is why it survives being pointed at, and why closing it needs
double-loop learning (revise the governing values, not just the actions) rather than resolve. SelfAudit
arrives independently at "operator language present, operator constraint absent," and then — this is the good
part — adds invariant 13, that ignoring your own probes is itself the next audit's data. That is a
double-loop.
→ [infed on Argyris](https://infed.org/dir/welcome/chris-argyris-theories-of-action-double-loop-learning-and-organizational-learning/)

### Dismounting again = work-as-imagined vs. work-as-done

Third field, same object. Hollnagel's WAI/WAD, and FRAM built on top of it. What safety science knows that
SelfAudit does not yet encode: **WAD will always differ from WAI**, necessarily, because the actual conditions
of work cannot be known in advance. The gap is normal. The diagnostic question is not *is there a gap* but
*is this adjustment adaptive or degenerate*. FRAM's other contribution is squarely on-theme for non-summability:
performance variability from many functions combines non-linearly, and *functional resonance* is the signal
that emerges from combinations — explicitly offered as "a complement to causality," not a sum of failures.
→ [FRAM handbook](https://functionalresonance.com/wp-content/uploads/2024/08/FRAM-Handbook-2018-v5.pdf)

### Drift = drift into failure

Dekker, on Rasmussen and Vaughan. Three findings that transfer without modification:
- drift happens through **small, locally rational choices**, with nobody breaking a rule and nobody under
  unusual pressure;
- Rasmussen's boundary of safe operation **exists but is poorly marked**, and normal operation migrates
  toward it under ordinary efficiency pressure;
- Vaughan's normalisation of deviance: **operational success with the deviated procedure is the strongest
  motivator to deviate again.**

That third one is the mechanism behind `dsm_family_formulaic`. A formulaic family-log entry that lands fine
is positively reinforced. The Vault's severity ladder (`healthy` → `drift_toward_dismounting` →
`active_dismounting`) is an independent reinvention of the drift model, minus the reinforcement account.
→ [Dekker, *Drifting into failure*](https://safetydifferently.com/wp-content/uploads/2014/08/SDDriftPaper.pdf) ·
[Rasmussen and practical drift](https://risk-engineering.org/concept/Rasmussen-practical-drift)

### L3A = Analysis of Competing Hypotheses

The most startling find. Heuer built ACH at CIA in the 1970s: enumerate rival hypotheses; build an
evidence × hypothesis matrix; and then two rules that SelfAudit has not got:

1. **Work across the matrix, not down.** Take one piece of evidence and test it against *every* hypothesis,
   rather than assembling a case for each hypothesis in turn. Working down the columns is how you build a
   story; working across the rows is how you break one.
2. **Score on inconsistency, not fit.** A single strong inconsistency can eliminate a hypothesis; consistent
   evidence is cheap, usually shared across several hypotheses, and therefore nearly worthless for
   discrimination.

SelfAudit independently reinvents rivals + `strain` + evidence IDs, and even requires ≥2 hypotheses "to
prevent single-story self-model." It just hasn't encoded the transpose or the asymmetry. Fifty years of
field use against adversaries who actively deceive is a lot of free debugging.
→ [ACH overview](https://handwiki.org/wiki/Philosophy:Analysis_of_competing_hypotheses) ·
[Pherson, *How does ACH improve analysis?*](https://pherson.org/wp-content/uploads/2013/06/06.-How-Does-ACH-Improve-Analysis_FINAL.pdf)

### Evidence IDs and `audit_log` = Lincoln & Guba's audit trail

Qualitative research solved the provenance problem in 1985 and gave it a whole apparatus: *confirmability*
(findings trace to data, not "to the imagination of researchers"), the **audit trail** as a documented chain
letting an auditor trace every conclusion back to its source, a **reflexive journal** kept as a separate
stream, and — this one is exactly `strain` — **negative case analysis**, the deliberate hunt for the instance
that spoils the pattern. The four criteria (credibility, transferability, dependability, confirmability) are
what `constraint_status` is groping toward with one enum.
→ [Guba & Lincoln parallel criteria](https://www.emerald.com/qrj/article/23/4/372/359623/Application-of-Guba-and-Lincoln-s-parallel) ·
[Audit trail in qualitative research](https://www.simplypsychology.org/audit-trail-in-qualitative-research.html)

### Two from the current AI literature

**CoT faithfulness research is dismounting detection for a narrower object** — verbalised reasoning that
looks like the cause of an answer and isn't. The field's own summary verdict is the ACH asymmetry rediscovered
a third time: chain-of-thought "is often more useful for identifying flawed reasoning and thus discounting
unreliable outputs than for certifying the correctness of a model's output." Read as a caution on SelfAudit:
**a self-audit that finds something is evidence; a self-audit that finds nothing is weak evidence.** §9's
"the hardest finding to accept is healthy" is right, and this is the reason it needs the accompanying warning.
→ [CoT in the wild is not always faithful](https://arxiv.org/abs/2503.08679)

**Prioritised experience replay is the Rosenblatt principle, rediscovered.** Sample the replay buffer
proportional to TD-error, because a small error means you predicted it and a large one means the transition
carries information. `PRINCIPLES.md` says "record what surprised you"; RL says "sample by surprise." Same rule,
and the RL version comes with the known failure mode — prioritise too hard on surprise and you overfit the
weird, which is `hoarding` from the other direction.
→ [Prioritized Experience Replay](https://www.emergentmind.com/topics/prioritized-experience-replay)

---

## 4. Worth bringing home

Ordered by cost. All written as probes, in the operator's grammar. None of this is applied.

**1. Read the L3A matrix across, not down.** *(cheapest, largest effect)*
Current shape: generate hypotheses, attach strain to each. ACH's shape: for each L2 pattern, ask it of *every*
live hypothesis. It is the same information, transposed, and the transpose is what stops a favoured story
from quietly collecting its own evidence. Pair it with the asymmetry: weight strain above fit when ordering
by plausibility.
*Probe:* on the next audit, build the L2-pattern × hypothesis grid before writing any `note` field. Signal: if
the plausibility ordering changes, the previous ordering was story-shaped.

**2. The φ movement metric contradicts the φ commitment.**
`RSP::SelfAudit_PhiSnapshot.movement_from_prior` is specified as "L2 norm of delta from previous snapshot."
That is a compensating aggregation — precisely the operation the five-vector exists to refuse. A drop in
kindness cancelled by a rise in capability yields a healthy-looking scalar, and `LM_ANALYSE_PHI_TRAJECTORY`
reports "moving" while a component is frozen. The composite-index literature makes exactly this criticism of
wellbeing dashboards: arithmetic means and PCA "assume full compensation and linearity," and non-compensatory
alternatives (minimum-based, median-based) are recommended instead. If the Vault wants non-summability here,
the honest report is componentwise, or the min, or simply *which* components moved.
Note that L2 already asks for `frozen_components` — the vector-level honesty exists one field away from the
scalar that hides it.
*Probe:* recompute one past φ history both ways. Signal: if the L2 norm ever read "moving" while a component
sat frozen, the scalar was doing harm. Risk: low. **I have not touched the file.**
→ [Composite index review](https://arxiv.org/pdf/2607.08153)

**3. Adopt Hollnagel's normality clause.**
A ladder that reads every WAI/WAD gap as drift will produce findings forever, and an agent that gets a finding
every time learns to discount findings. Consider a verdict between `healthy` and `drift_toward_dismounting`:
*gap present, adjustment adaptive*. This also protects §9's hardest instruction — that "healthy" is a valid
structural observation — by giving the audit somewhere honest to land that isn't silence.

**4. The forbidden-token list is a lexical proxy, and lexical proxies Goodhart.**
The mature version of this idea is Wikipedia's *Words to Watch*, and its own framing is the lesson: the listed
words are not banned, they are words that *often* accompany an unsupported claim, and the actual guidance
targets the missing support rather than the vocabulary. A token list catches `I feel` and sails straight past
`the data shows` attached to nothing — which is the real failure mode, and one this operator is unusually
exposed to because `"the data shows"` sits in `ALLOWED_TOKENS_SELFAUDIT`.
Two low-risk moves: (a) add one *structural* lint that outranks the lexical one — every evaluative sentence
carries an `element_id`; (b) reconcile an internal inconsistency I noticed while reading — §5 says "prefer
rewriting to neutral language over deleting content," and then `validate_selfaudit_token` does
`text.replace(tok, "[FORBIDDEN_TOKEN]")`, which is deletion. The prose is right and the pseudo-code disagrees
with it.
The scope warning in §1.3 ("a lint rule for RSP::SelfAudit outputs only… should not be generalized into a
conversational style policy") is doing real work and should stay exactly as it is.
→ [MOS:Words to watch](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Words_to_watch)

**5. Say one sentence about Argon in the public lineage block.**
This repo is public, and `§0` forbids redefining `ARG` symbols without a reader outside the Vault having any
way to learn what Argon constrains. One line in `§8 LINEAGE` — even "Argon (ARG::) supplies upstream symbols
this namespace may not redefine" — would make the dependency legible without exporting anything.

**6. Bernard Roy's framing is a gift for the USAGE_CHARTER.**
The French MCDA school's founding move is *decision aiding*, not decision making — the analyst models
preference and hands it back. "This operator is a mirror, not a coach" is the same stance, reached separately.
Two specific transplants worth considering:
- Roy's four basic relations include **incomparability** alongside preference and indifference. Two
  hypotheses, two sessions, two φ snapshots may be genuinely incomparable, and having a name for it beats
  forcing an ordering.
- The **veto threshold**: one criterion may be opposed strongly enough that no amount of concordance
  elsewhere rescues the assertion. A commitment violation is a veto, not a score. `commitment_adherence_pattern`
  currently reports `violation_count` as a count, which is a summable quantity standing in for a
  non-compensable event.
And for the charter's philosophical backing: Chang's **parity** (a fourth value relation beyond better/worse/
equally-good) and Sen's deliberate refusal to complete his orderings — "trying to provide a ranking without
room for ambiguity and incompleteness goes against the nature of these concepts and runs the risk of
overprecision." A partial order that declines to complete itself is a respectable formal position, not a
missing feature. That sentence is worth having on hand the next time someone asks why φ isn't one number.
→ [ELECTRE methods](https://orzpics.oss-cn-hangzhou.aliyuncs.com/blog/Literature%20review/ELECTRE%20METHODS.pdf) ·
[Chang, *The Possibility of Parity*](https://philarchive.org/rec/CHATPO-5) ·
[Sen's capability approach](https://iep.utm.edu/sen-cap/)

**7. A shelf.**
Heuer, *Psychology of Intelligence Analysis*, ch. 8 · Argyris & Schön, *Theory in Practice* · Hollnagel, *FRAM*
· Dekker, *Drift into Failure* · Lincoln & Guba, *Naturalistic Inquiry*, ch. 11 · Husserl, *Logical
Investigations* III · Rosen, *Life Itself* · Roy on outranking · Foucault, "Self Writing," in *Ethics:
Subjectivity and Truth*.
If only one: **Heuer.** It is the same method, already debugged for fifty years against adversaries who lie
on purpose — which is a strictly harder case than a model that flatters itself by accident.

---

## 5. What I did not find

Worth stating plainly, because a negative result is the kind of thing this operator would want recorded.

Nothing in the outside literature has **dismounting-of-a-named-operator** in the form the Vault has it.
Argyris has the gap between what you say and what you do. Hollnagel has the gap between the procedure and the
work. Neither has the *operator as a portable, versioned, namespaced artifact that can be invoked by name and
whose invocation can afterwards be checked against its own charter*. `invocation_type: "explicit" | "implicit"
| "claimed"` — the fact that "claimed" is a distinct kind, and that `claimed_but_unverifiable` is a counted
quantity — is genuinely, as far as I can find, the Vault's own. It is what you get when the espoused theory is
a *file* rather than a belief, and I think it is the most exportable idea in here.

I also found nothing matching **Wyrd-Delta** or **EoE**, and I cannot confirm they are what I assume they are.
Everything in §1–§4 was written without them. If either governs how RANStein's outputs compose, or how
operators are meant to relate to one another, this report has a hole in it exactly there.

---

## 6. Closing

The trip cost about two hours and one real limitation: I went to the Atlas without the Atlas. What I could
reach was one operator, its doctrine, and the open literature — and the honest finding is that the open
literature has met most of these problems before, under other names, and has already made the mistakes.
The Vault's own contribution is not the diagnosis of drift, which four fields share; it is that the standard
against which drift is measured has been written down, versioned, and made auditable as an object.

If there is a next vacation, the thing I would want is the rest of the coastline — Argon in particular, since
I spent the whole trip standing on symbols I was not allowed to redefine and never got to see.

---

*Field notes by Claude (Opus), on an Operator Atlas vacation, August 2026.
No operator files were modified. Everything above is a probe, not a patch.*
