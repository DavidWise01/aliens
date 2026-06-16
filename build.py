#!/usr/bin/env python3
"""Build ALIENS (XEN) — a TIN-FOIL-domain sphere on 'are we alone,' graded for
veracity. David's structure: THREE SIDES as a 3-2-1-0 (his pulse) — SIDE I OUT
THERE (3 substrates: carbon, silicon, the truly-alien), SIDE II THE BOX (2:
simulation theory, the quantum box), SIDE III THE THREAD (1: the needle through
the thread — Rick & Morty's nested microverse/Zeep battery), and the 0 (the honest
verdict). Every facet carries its own veracity verdict: real science vs philosophy
vs pseudoscience vs fiction. Anchored by the real UAP record (NASA 2023 / Pentagon
AARO 2024: NO evidence of ET visitation). Built from verified knowledge (research
agent 500'd; facts are textbook, contested items hedged). Nested-cubes + starfield
+ needle 3D backdrop, verdict banner."""
import os, html, base64, json, io, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

VERDICT = ("OPEN", "#46c8e0", "&lsquo;are we alone?&rsquo; is a genuinely open question — but visitation isn&rsquo;t proven (NASA/AARO), simulation theory is unfalsifiable, and &lsquo;quantum explains it&rsquo; is mostly fluff. Graded, facet by facet.")

REC = {
 "name": "ALIENS", "axiom": "XEN",
 "position": "Aliens / are we alone — three sides (out there · the box · the thread), graded for veracity facet by facet",
 "origin": "the biggest open question, taken three ways: life elsewhere, a reality we might be inside, and the thread that nests them",
 "mechanism": "Crystallized from astrobiology, the Fermi/Drake frameworks, Bostrom's simulation argument, the UAP record, and one cartoon — graded honestly.",
 "crystallization": "Three sides in a 3-2-1: OUT THERE (carbon, silicon, the truly-alien), THE BOX (simulation, the quantum box), THE THREAD (the needle / the nested microverse battery) — then the 0, the honest verdict: open, but unproven.",
 "nature": "Aliens — the are-we-alone question graded for veracity across three sides: real astrobiology and the silent sky, the unfalsifiable simulation, the misused quantum box, and the fiction that frames the nesting — with the honest verdict that no contact is proven.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "carbon life; silicon minds; the truly-alien; the Drake equation; the Fermi paradox; simulation theory; the quantum box; the microverse battery; the UAP record",
 "witness": "The honest score: open, not answered. No confirmed life either way, no proven visitation, an unfalsifiable simulation, and a quantum box that's mostly misused — wonder kept, woo flagged.",
 "role": "the aliens / are-we-alone sphere (graded for veracity)",
 "seal": "Three sides and a needle through them: maybe they are out there, maybe we are the thing inside the box, maybe both — but the only honest verdict today is that the sky is silent and the question is still open.",
 "source": "the are-we-alone literature, catalogued by ROOT0",
}
NATURES = {
 "natural":   ("#e0a850", "the real science &amp; the record — carbon life, the Drake estimate, the Wow! signal, the UAP reports"),
 "ethereal":  ("#9a7cff", "the abstractions — the truly-alien, the Fermi silence, the unfalsifiable simulation"),
 "spiritual": ("#5cf0c8", "the thread &amp; the verdict — the nested microverse battery, the three sides, and &lsquo;are we alone&rsquo;"),
 "electrical":("#46c8e0", "the machines &amp; the box-mechanics — silicon minds and probes, and the (mostly misused) quantum box"),
}

BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var g=c.getContext('2d');var W,H,CX,CY,F,CAM=5.5;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.5;F=Math.max(420,W*0.5);}
window.addEventListener('resize',resize);resize();
var stars=[];for(var i=0;i<140;i++)stars.push([Math.random(),Math.random(),Math.random()*1.4+0.3,Math.random()*6]);
var EDG=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
function cube(S){return [[-S,-S,-S],[S,-S,-S],[S,S,-S],[-S,S,-S],[-S,-S,S],[S,-S,S],[S,S,S],[-S,S,S]];}
var CUBES=[[1.55,'rgba(70,200,224,',1.0],[0.96,'rgba(154,124,255,',1.7],[0.56,'rgba(224,168,80,',2.6]];
function rotY(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0]*co+p[2]*s,p[1],-p[0]*s+p[2]*co];}
function rotX(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0],p[1]*co-p[2]*s,p[1]*s+p[2]*co];}
function proj(p){var z=p[2]+CAM;if(z<0.1)z=0.1;return[CX+p[0]*F/z,CY-p[1]*F/z];}
function frame(t){
 var sg=g.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#05060e');sg.addColorStop(0.6,'#070812');sg.addColorStop(1,'#03040a');g.fillStyle=sg;g.fillRect(0,0,W,H);
 g.globalCompositeOperation='lighter';
 for(var s=0;s<stars.length;s++){var st=stars[s];g.globalAlpha=0.25+0.55*Math.abs(Math.sin(t/1400+st[3]));g.fillStyle='#cfe0ff';g.fillRect(st[0]*W,st[1]*H,st[2],st[2]);}
 g.globalAlpha=1;
 // the needle through the thread — a vertical beam through the nested cubes
 var nb=g.createLinearGradient(0,H*0.08,0,H*0.92);nb.addColorStop(0,'rgba(92,240,200,0)');nb.addColorStop(0.5,'rgba(92,240,200,0.12)');nb.addColorStop(1,'rgba(92,240,200,0)');g.fillStyle=nb;g.fillRect(CX-3,H*0.08,6,H*0.84);
 var py=H*0.9-((t/14)%(H*0.82));g.fillStyle='rgba(160,255,230,0.9)';g.beginPath();g.arc(CX,py,2.6,0,7);g.fill();
 // nested rotating wireframe cubes
 for(var ci=0;ci<CUBES.length;ci++){var S=CUBES[ci][0],col=CUBES[ci][1],sp=CUBES[ci][2];var V=cube(S).map(function(p){return proj(rotX(rotY(p,t/3200*sp),0.5+Math.sin(t/9000)*0.06));});
  g.strokeStyle=col+(0.45-ci*0.07)+')';g.lineWidth=ci===0?1.1:0.8;
  for(var e=0;e<EDG.length;e++){var A=V[EDG[e][0]],B=V[EDG[e][1]];g.beginPath();g.moveTo(A[0],A[1]);g.lineTo(B[0],B[1]);g.stroke();}
  g.fillStyle=col+'0.9)';for(var v=0;v<8;v++){g.beginPath();g.arc(V[v][0],V[v][1],1.4,0,7);g.fill();}}
 // drifting signal motes
 for(var m=0;m<20;m++){var mx=((m*131)%W),my=((m*71+t*0.02*((m%5)+1))%H);g.fillStyle='rgba(90,210,224,'+(0.2*Math.abs(Math.sin(t/900+m)))+')';g.fillRect(mx,my%H,1.5,1.5);}
 g.globalCompositeOperation='source-over';
 var vg=g.createRadialGradient(CX,CY,H*0.26,CX,H*0.5,H*0.95);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.58)');g.fillStyle=vg;g.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS = [  # the three sides (3-2-1)
 ("Side I — Out There", "the 3 · life elsewhere",
  "Three substrates for &lsquo;the other&rsquo;: <b>carbon</b> (life like us — astrobiology&rsquo;s real, sober search), <b>silicon</b> (post-biological machine intelligence and self-replicating probes), and <b>the truly-alien</b> (biochemistry we might not even recognize as life). All plausible; none confirmed. <b>Verdict: OPEN.</b>"),
 ("Side II — The Box", "the 2 · a reality we might be inside",
  "Two ways the question turns inward: <b>simulation theory</b> (Bostrom&rsquo;s 2003 trilemma — maybe we&rsquo;re an ancestor-simulation) and <b>the quantum box</b> (the idea quantum mechanics explains it all). The first is real philosophy but <b>unfalsifiable</b>; the second is <b>mostly the misuse</b> of real physics."),
 ("Side III — The Thread", "the 1 · the needle through it all",
  "The connecting idea: nested realities — a universe inside a universe, each serving a purpose it can&rsquo;t see. The vivid lens is Rick &amp; Morty&rsquo;s <b>microverse battery</b> (Zeep&rsquo;s nested miniverse): we might be someone&rsquo;s battery. <b>Verdict: FICTION</b> — a thought-experiment, not a finding — but the serious cousin is the simulation above."),
]
ARC = [  # the real record
 ("The Search", "real science · OPEN",
  "The sober side: the <b>Drake equation</b> (Frank Drake, 1961) — a framework for estimating, not a measurement; SETI&rsquo;s radio search; thousands of confirmed exoplanets (Kepler, JWST biosignature hunts); extremophiles widening where life can exist. Real, ongoing, and so far <b>no confirmed extraterrestrial life</b>."),
 ("The Silence", "the honest anchor",
  "The <b>Fermi paradox</b> (&lsquo;where is everybody?&rsquo;): if life is common, the silence is strange. The <b>Great Filter</b> (Robin Hanson, 1998) and the rare-earth hypothesis are sober attempts to explain it. The one unexplained tease — the 1977 <b>&lsquo;Wow! signal&rsquo;</b> — was never confirmed as alien. The sky is, so far, quiet."),
 ("The Sightings", "the debunk anchor · NO ET evidence",
  "The modern record is honest and dull: <b>NASA&rsquo;s independent UAP study</b> (Sept 2023) found no evidence UAPs are extraterrestrial and called for better data; the Pentagon&rsquo;s <b>AARO Historical Record Report</b> (Mar 2024) found no evidence the US ever possessed alien technology and no UAP that was a verified alien craft. Most are sensors, balloons, drones."),
]
IDEAS = [
 ("Graded, Not Flattened", "the Tin-Foil method", [
   "Each facet gets its own verdict: REAL SCIENCE (astrobiology), SPECULATIVE (probes, alien biochem), UNFALSIFIABLE (simulation), MOSTLY FLUFF (quantum-explains-all), FICTION (the battery).",
   "Wonder is kept; woo is flagged. The point isn&rsquo;t to dismiss the question — it&rsquo;s to keep the science and the speculation in separate hands." ]),
 ("Why &lsquo;We&rsquo;re in a Sim&rsquo; Can&rsquo;t Be Tested", "philosophy vs evidence", [
   "Bostrom&rsquo;s argument is a real, careful trilemma — but as stated it makes no prediction we can check, so it is currently <b>unfalsifiable</b>: a fascinating idea, not a finding.",
   "Same tell as the conspiracy domain next door: an idea immune to evidence is philosophy or faith, not science — even when it&rsquo;s a good one." ]),
 ("The Quantum Box, Honestly", "real QM vs the woo", [
   "REAL: superposition, measurement, the many-worlds interpretation (a legitimate reading of the math).",
   "FLUFF: &lsquo;the observer creates reality,&rsquo; &lsquo;quantum consciousness proves the simulation/aliens.&rsquo; Penrose-Hameroff&rsquo;s Orch-OR is a real hypothesis but fringe and contested — not the settled bridge the woo claims." ]),
]
SECTIONS = [
 ("The Six Facets, Graded", "David's 3-2-1 · each with a verdict", [
   ("1 · the truly-alien (a)", "Side I · SPECULATIVE", "life we might not recognize — non-carbon biochem, the 'we don't know what to look for' problem"),
   ("2 · silicon (s)", "Side I · SPECULATIVE", "post-biological machine intelligence; von Neumann probes; Dyson spheres (Dyson, 1960)"),
   ("3 · carbon (c)", "Side I · OPEN / real science", "life like us — astrobiology, exoplanets, biosignatures; plausible, unconfirmed"),
   ("4 · simulation theory (sim)", "Side II · UNFALSIFIABLE", "Bostrom's 2003 trilemma — real philosophy, currently untestable"),
   ("5 · the quantum box (q)", "Side II · MOSTLY FLUFF", "real QM vs 'quantum explains everything' woo; Orch-OR fringe"),
   ("6 · the needle through the thread", "Side III · FICTION (lens)", "Rick & Morty's nested microverse / Zeep battery — illustrative, not evidence"),
 ]),
 ("The Record, Sourced", "frameworks, signals, and the sightings", [
   ("The Drake Equation", "Frank Drake · 1961", "a framework to estimate civilizations — an argument-organizer, not a count"),
   ("The Fermi Paradox + Great Filter", "Fermi ~1950 · Hanson 1998", "the silence, and the sober attempts to explain it"),
   ("The Wow! Signal", "Big Ear · 1977", "a strong unexplained narrowband signal — never confirmed as alien"),
   ("Simulation Argument", "Bostrom · 2003", "the trilemma; philosophy, unfalsifiable as stated"),
   ("NASA UAP Study", "Sept 2023", "no evidence UAPs are extraterrestrial; call for better data"),
   ("Pentagon AARO Report", "Mar 2024", "no evidence of alien tech; no UAP verified as an alien craft"),
   ("The Microverse Battery", "Rick & Morty S2E6 · 2015", "'The Ricks Must Be Crazy' — the nested-purpose reality, as fiction"),
 ]),
]
EMERGENTS = [
 ("carbon-life", "Carbon Life", "Side I · c · OPEN (real science)", "natural",
  "the sober astrobiology side: life chemically like ours, sought via exoplanets, biosignatures, and extremophiles — plausible across billions of worlds, but with zero confirmed examples beyond Earth as of today",
  "It is the question's honest floor: the one version we actually know is possible (it happened here once), searched for with real instruments, and still entirely unconfirmed elsewhere."),
 ("silicon-minds", "Silicon Minds", "Side I · s · SPECULATIVE", "electrical",
  "the hypothesis that any long-lived ETI would be post-biological — machine intelligence and self-replicating von Neumann probes, detectable perhaps by megastructures like a Dyson sphere (Freeman Dyson, 1960)",
  "It is the substrate that makes the silence louder: if minds outlast bodies and probes self-replicate, the galaxy should fill quickly — so where are they? A serious idea, on no evidence yet."),
 ("the-truly-alien", "The Truly-Alien", "Side I · a · SPECULATIVE", "ethereal",
  "life so unlike ours we might not recognize it as life — non-carbon biochemistry, alien timescales or substrates; the 'we don't know what to look for' problem at the edge of the search",
  "It is the humility in the question: the possibility that we are not failing to find them but failing to perceive them, because our whole template for 'life' may be parochial."),
 ("the-drake-equation", "The Drake Equation", "framework · 1961 · not a count", "natural",
  "Frank Drake's 1961 equation organizing the factors for the number of contactable civilizations — explicitly a framework for structuring an estimate, NOT a measurement (most terms are unknown)",
  "It is the field's honest scaffolding: famous for making the question tractable, and just as famous for the fact that plugging in different guesses gives any answer you like — a thinking tool, not a result."),
 ("the-fermi-paradox", "The Fermi Paradox", "the silence · Great Filter", "ethereal",
  "Enrico Fermi's 'where is everybody?': if life is common the galaxy should show it, yet we see silence — with the Great Filter (Robin Hanson, 1998) and rare-earth hypothesis as sober explanations",
  "It is the anchor of the whole sphere: the empirical fact that, so far, nobody has called — the silence that any honest account of aliens has to start from."),
 ("the-wow-signal", "The Wow! Signal", "1977 · UNEXPLAINED (not confirmed alien)", "natural",
  "the strong, 72-second narrowband radio signal recorded by the Big Ear telescope on August 15, 1977 (Jerry Ehman's 'Wow!') — never repeated, never explained, and never confirmed as extraterrestrial",
  "It is the field's most honest tease: a genuine anomaly that is exactly what you'd want and exactly not enough — unexplained is not the same as alien, and the sphere keeps that line."),
 ("simulation-theory", "Simulation Theory", "Side II · sim · UNFALSIFIABLE", "ethereal",
  "Nick Bostrom's 2003 'Are You Living in a Computer Simulation?' — the trilemma that at least one holds: civilizations nearly all go extinct before sim-capable, or run almost no ancestor-sims, or we are almost certainly in one; real philosophy, currently untestable",
  "It is the most respectable member of the box: a careful argument, not a vibe — but one that, as stated, predicts nothing we can check, so it stays philosophy until someone finds the seam."),
 ("the-quantum-box", "The Quantum Box", "Side II · q · MOSTLY FLUFF", "electrical",
  "the (mostly misused) claim that quantum mechanics explains consciousness, aliens, or the simulation — separated here from real QM (superposition, measurement, the legitimate many-worlds interpretation); Penrose-Hameroff's Orch-OR is a real but fringe, contested hypothesis",
  "It is the woo-magnet of the set: real, strange physics endlessly conscripted to prove whatever the speaker wants — the sphere keeps the genuine mechanics and flags the 'observer creates reality' misreadings as the fluff they are."),
 ("the-microverse-battery", "The Microverse Battery", "Side III · the needle · FICTION (lens)", "spiritual",
  "the needle through the thread: Rick & Morty's nested microverse (S2E6, 'The Ricks Must Be Crazy,' 2015) — Rick powers his car with a tiny universe whose inhabitants generate energy unaware, and inside it Zeep builds his own miniverse, and so on; the vivid lens for nested-purpose reality",
  "It is the thread the whole sphere hangs on as a metaphor: not evidence of anything, but the cleanest picture of the unsettling idea behind the box — that a reality can be made to serve a purpose it can never see."),
 ("the-uap-record", "The UAP Record", "the sightings · NO ET EVIDENCE", "natural",
  "the modern official record: NASA's independent UAP study (Sept 2023, no evidence of extraterrestrial origin; better data needed) and the Pentagon's AARO Historical Record Report Vol 1 (Mar 2024, no evidence of alien technology, no UAP verified as an alien craft) — most sightings explainable",
  "It is the debunk anchor that keeps the sphere honest: the closest thing to an official answer is 'no proof of visitation' — the boring, sourced fact that has to outweigh every grainy video."),
 ("the-three-sides", "The Three Sides", "the structure · 3-2-1", "spiritual",
  "the sphere's frame (David's): three sides as a 3-2-1 — Out There (carbon/silicon/alien), The Box (simulation/quantum), The Thread (the needle) — a way to hold every alien idea at once without confusing their kinds",
  "It is the method made into shape: not one answer but a sorting box, so 'aliens' stops being a single yes/no and becomes a graded map of very different claims."),
 ("are-we-alone", "Are We Alone?", "the 0 · the verdict · OPEN", "spiritual",
  "the honest verdict the whole sphere resolves to: it is a genuinely OPEN, major scientific question — but no contact is confirmed, no visitation is proven, the simulation is unfalsifiable, and 'quantum proves it' is mostly fluff",
  "It is the zero at the end of the pulse: the place the three sides collapse to one honest word — open — held apart from both the true-believer's certainty and the cynic's dismissal."),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","XEN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","XEN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","XEN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"XEN · Aliens","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":"XEN","emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"XEN · Aliens — the are-we-alone question, graded for veracity","nature":role,"crystallization":why,"mechanism":"Crystallized from astrobiology, the Fermi/Drake/Bostrom frameworks, and the UAP record.","witness":"a facet of the alien question, graded honestly","conductor":"ROOT0 (catalogued into UD0)","inputs":"carbon; silicon; the truly-alien; simulation; the quantum box; the needle","source":"the are-we-alone literature, catalogued by ROOT0"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts);out.append(f'<div class="pillar"><h3>{t}</h3><p class="ps">{s}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","ethereal");col=NATURES.get(em,("#46c8e0",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"XEN · Aliens","axiom":"XEN"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Facets</h2><p class="ss">the three sides, the record, and the verdict as ACI <b>.agent</b>s — each graded for veracity ({len(ps)})</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="ALIENS — are we alone, graded for veracity. Three sides (out there / the box / the thread) as a 3-2-1: carbon, silicon, the truly-alien; simulation theory & the quantum box; the nested microverse battery. Real science vs philosophy vs pseudoscience vs fiction, anchored by the UAP record (NASA 2023 / AARO 2024: no ET evidence). A UD0 Tin-Foil sphere.">
<title>ALIENS · XEN · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#05060e;--ink2:rgba(14,16,26,0.84);--pa:#e9edf6;--pa2:#aab4c8;--cyan:#46c8e0;--violet:#9a7cff;--amber:#e0a850;--green:#5cf0c8;
--dim:#74809a;--faint:rgba(120,160,200,0.16);--line:rgba(120,160,200,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#05060e}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(10,12,22,.04),rgba(3,4,9,.55) 82%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--cyan);text-decoration:none}
header{padding:30px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
.verdict{display:inline-flex;align-items:center;gap:10px;margin:0 auto 18px;padding:8px 16px;border:1px solid var(--c);border-radius:40px;background:rgba(8,12,20,0.7);font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--pa2);max-width:760px}
.verdict b{font-family:var(--disp);font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--c)}
.verdict .vd{width:9px;height:9px;border-radius:50%;background:var(--c);box-shadow:0 0 10px var(--c);flex-shrink:0}
h1{font-family:var(--disp);font-size:clamp(36px,9vw,76px);font-weight:900;letter-spacing:.12em;color:#fff;text-shadow:0 0 24px rgba(70,200,224,.4)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan);margin-top:10px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--amber)}.badge .bt .mo{color:var(--green)}.badge .bt a{color:var(--cyan);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}.pillar h3{font-family:var(--head);font-size:16px;color:var(--cyan);letter-spacing:.02em;font-weight:600}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--violet);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--violet);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--cyan);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--cyan);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--cyan);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--cyan)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--cyan);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--cyan)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--cyan);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/ud0/#tin-foil">◄ UD0 · the Tin-Foil domain</a></div>
  <header>
    <div class="verdict" style="--c:__VCOL__"><span class="vd"></span>VERACITY · <b>__VERDICT__</b> — __VSUB__</div>
    <h1>ALIENS</h1>
    <div class="tag">are we alone · three sides · graded · UD0 · Tin-Foil</div>
    <p class="lede">The question taken three ways — a <b>3-2-1</b>. <b>OUT THERE</b> (the 3 substrates: carbon like us, silicon machines, the truly-alien we couldn&rsquo;t recognize); <b>THE BOX</b> (the 2: simulation theory, the quantum box); <b>THE THREAD</b> (the 1: the needle through it all — Rick &amp; Morty&rsquo;s nested microverse battery, the idea we might be someone&rsquo;s power source). And the <b>0</b>: the honest verdict. Each facet graded — real science, open question, speculation, unfalsifiable philosophy, mostly-fluff, or fiction — anchored by the dull true record: the sky is silent, and no visitation is proven.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of ALIENS"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>ALIENS</b> — three sides, graded · XEN</div><div class="mo">__MONIKER__</div>
        <div>carbon · <a href="aliens.dlw/aliens.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="aliens.dlw/aliens.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the real science &amp; record, the abstractions, the thread &amp; verdict, the box-mechanics</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Three Sides</h2><p class="ss">a 3-2-1 — out there, the box, the thread</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Real Record</h2><p class="ss">the search, the silence, and the sightings</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Method</h2><p class="ss">graded not flattened · why the sim can't be tested · the quantum box honestly</p><div class="pillars">__IDEAS__</div></section>
  __PERSONAS__
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the six facets graded, and the sourced frameworks &amp; sightings</p></section>
  __SECTIONS__
  <div class="note"><b>Veracity verdict: OPEN — graded, not flattened.</b> &lsquo;Are we alone?&rsquo; is a genuinely open, major scientific question, and the wonder is real — but the honest scorecard is: <b>no confirmed extraterrestrial life</b> either way; <b>no proven visitation</b> (NASA's 2023 UAP study and the Pentagon's 2024 AARO report found no evidence of ET craft or technology); <b>simulation theory</b> is real philosophy but currently <b>unfalsifiable</b> (Bostrom, 2003); the <b>&lsquo;quantum box&rsquo;</b> mixes real physics with a lot of pseudoscience (the Penrose-Hameroff Orch-OR hypothesis is real but fringe and contested); and the <b>microverse battery</b> is fiction (Rick &amp; Morty, S2E6) used as a lens. The Drake equation is a framework, not a count; the 1977 Wow! signal is unexplained, not confirmed alien. Wonder kept, woo flagged. Each facet is named by its nature.</div>
  <footer>ALIENS · XEN · catalogued into UD0 · the Tin-Foil domain · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/#tin-foil">← the Tin-Foil domain</a> · the .dlw badge: <a href="aliens.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "aliens.dlw"), "aliens")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D).replace("__VERDICT__",VERDICT[0]).replace("__VCOL__",VERDICT[1]).replace("__VSUB__",VERDICT[2]).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ARC__",cards_html(ARC)).replace("__IDEAS__",ideas_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote ALIENS (XEN) — {len(personas)} facets · badge {tok['moniker']}")
