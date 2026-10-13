# STORMBREAKER SOUL — Deepwoken PvP Build

*Built for the live game as of **October 2026 (patch 3.2.21a)**. Every stat requirement and talent effect below was taken from the Deepwoken Builder database (deepwoken.co) and the official fan wiki, then checked against all 2025–2026 balance changes. See [`research/META_RESEARCH_2026-10.md`](research/META_RESEARCH_2026-10.md) for the evidence.*

> **One-line pitch:** A Thundercall/Stormseye duelist that makes opponents hit you for **half damage** (Electrified), takes **reduced PEN** (Reinforced Armor), **refuses to die** (Tidekeeper → Jumper Cables → Immortality), and cashes out with Ardour Scream + Manipulator crits and Surge overloads.

---

## Quick card

| Slot | Pick | Why |
|---|---|---|
| **Race** | **Vesperian** (+3 FTD, +2 WLL) | Chitin = 5% physical DR as natural armor, stacks with Exoskeleton. Both stat bonuses are used. |
| **Origin** | **Lone Warrior** | Mark of the Lone Warrior: damage boost when alone **or outnumbered**. Castaway is fine if you don't have it unlocked. |
| **Oath** | **Soulbreaker** | Community S-tier (4.62/5, 1,148 votes). All 3 Murmurs, Ardour Scream window, i-frame Rhythm Advance, Tacet + Formless engage/escape. +2 Combat, +1 Wildcard slot, +5% PEN. |
| **Attunement** | **Thundercall** (Surge Path + Interrogator) | Highest-rated mantra pool (Rising Thunder 4.64, Thunder Kick 4.58, Jolt Grab 4.51). Galebreathe, Bloodrend and Eclipse Kick were all hit hard in Aug 2026. |
| **Weapon** | **Stormseye** (40 MED / 75 LTN) | Its M1s **proc Thundercall talents, including Interrogator**. Its crit gives **full i-frames** and deals 2.22× scaled damage. Aerial M1s teleport behind targets. |
| **Outfit** | **Celtorian Tideknight** (alt: Black Diver) | Tidekeeper: lose 25% HP in 3s → +15% dmg, +20% defense, **cannot be knocked for 10s** (60s cooldown). |
| **Murmur** | Ardour + Tacet + Rhythm (all granted by Soulbreaker) | You need any one Murmur *before* taking the Oath. |
| **Resonance** | **Blood Scourge** for open world; **Payback** for Chime 2v2/3v3 | Resonances are disabled in Chime 1v1. |
| **Traits** | **Vitality 6 / Proficiency 6** | +60 HP; +39% weapon scaling and +15% weapon PEN. |
| **Boons** | Steadfast, Autodidact | |
| **Flaws** | Squeamish, Glutton | Low impact. Avoid **Obvious**: low stealth makes your Tacet bubble bigger, so more people can see you. Also avoid Haemophilia, Deficient and Simple. |

---

## 1. Final stats (Power 20, 330 points including race)

| Stat | Final | Purpose |
|---|---|---|
| **Fortitude** | **90** | Reinforced Armor (incoming PEN −30%), Exoskeleton, To The Finish, Mythic Stability, Defensive Reprisal. Needs *Fortitude Unbounded* (talk to Brutus at Fort Merit). |
| **Thundercall** | **80** | Stormseye requirement (75), Interrogator line (65), and **Level 5 mantras (needs 80)**. Needs *Thundercall Unbounded* (75 LTN + Master Thundercaller + kill any humanoid boss). |
| **Medium Weapon** | **40** | Stormseye requirement; enables Static Blade. |
| **Charisma** | **35** | Charm engine. Also Mind 35, which keeps Neuroplasticity's extra Wildcard slot. |
| **Willpower** | **30** | Perseverance (needed for Reinforced Armor), Underdog. CHA + WLL = 65, so you clear Soulbreaker's 50. |
| **Strength** | **20** | Spine Cutter, Matador, Concussion, Wyvern's Claw. Showstopper and Champion's Regalia come from the pre-shrine phase. |
| **Agility** | **20** | Observation, Safety Dance, Fast Blade. Ghost, Speed Demon and the other 25–45 AGL talents come from pre-shrine. |
| **Intelligence** | **15** | Static Link → **Jumper Cables** and Link Conduction. Also Ether Absorption. |

**Damage reference at final stats:**
- Stormseye M1 ≈ 19 × (1 + 0.75 × 600/1000 × 1.39) ≈ **31 per hit**, before multipliers.
- Crit ≈ **69** over 3 shots, with i-frames. About **82** if the target is Charmed (Manipulator).
- Weapon PEN ≈ 22%: 15 from Proficiency, 5 from the Oath, 2 from Strength.

**Health estimate:** 220 base + 4 + 60 (Vitality) + 35 (Fortitude) ≈ **319 before gear**. Expect **~360–410 with Health pips**.

---

## 2. Shrine of Order plan (do this BEFORE taking Soulbreaker)

Shrine of Order averages every stat you have at least 1 point in. Core and weapon stats can lose **at most 25** points; attunement stats can be averaged freely. The idea: pump talent-rich core stats first, take their talents, then let the shrine trade those points for Fortitude, Thundercall and Medium Weapon.

| Stat | Pre-shrine (≈ Power 9, 158 pts) | After shrine | Final |
|---|---|---|---|
| Charisma | **60** | 35 | 35 |
| Agility | **45** | 20 | 20 |
| Strength | **40** | 20 | 20 |
| Willpower | **7** (5 + 2 racial) | 20 | 30 |
| Fortitude | **4** (1 + 3 racial) | 20 | 90 |
| Medium Weapon | **1** | 20 | 40 |
| Thundercall | **1** | 20 | 80 |
| Intelligence | 0 (leave untouched) | 0 | 15 |

The shrine returns **3 free points**. After the shrine you invest the remaining 172 level-up points plus those 3 to reach the final column.

> Put at least 1 point into Fortitude and Willpower manually, or your racial points are not counted. If your attunement already has more than 1 point at shrine time, re-check the result in deepwoken.co's builder. It still works, but the numbers shift by 1–2.

**Order of play:**
1. **Power 1–9:** raise CHA → 60, AGL → 45 and STR → 40. Take every Charm, Agility and Strength talent listed in §3A as the cards come up.
2. **Power ≥ 8:** use **Shrine of Order** (costs 10 Knowledge, needs no Oath).
3. **Get a Murmur.** Easiest is **Tacet**: CHA 10 plus 5 bounty contracts. Ardour drops from the Dread Serpent or the Doom of Caeranthil.
4. **Take Soulbreaker.** *Method 2* is easiest: clear Duke Erisia's Manor, kill the Duke, and use a **Sinner's Ash** before you're teleported out. You need CHA + WLL ≥ 50, which you have (35 + 20). Finish progression with **5 shrine deals**; Shrine of Mastery and Conceit cost 1 Knowledge each.
5. **Level to the final stats:**
   - FTD 75 → Fortitude Unbounded → FTD 90.
   - LTN 75 → Thundercall Unbounded → LTN 80.
   - Then MED 40, INT 15 and WLL 30.
6. **Equip Stormseye once you have 40 MED and 75 LTN.** Until then, any medium sword works with Static Blade.

---

## 3. Talents (priority order)

### A. Pre-shrine: Charm, Agility, Strength
| Talent | Requirement | What it does for you |
|---|---|---|
| **Charismatic Cast** | CHA 25 | Every mantra hit Charms the target. Charmed targets deal 10% less to you. |
| **Tough Love** | CHA 25 | +10% weapon damage (+5% mantra) against targets you Charmed. |
| **Lasting Charisma / Chaotic Charm** | CHA 55 | Longer charms; a low-HP charm burst. Both are prerequisites for Dazing Finisher. |
| **Dazing Finisher** *(Advanced)* | CHA 55 + the four above | Flourishing a Charmed target **dazes them instead of knocking them away**, so the combo continues. |
| **Manipulator** | CHA 60 | **+20% critical damage** to Charmed targets. Pairs with Stormseye's 2.22× crit. |
| **Narcissist** | CHA 60 | Re-charming a Charmed target gives you Overcharm: every hit charms, and M1s deal +10%. |
| **Neuroplasticity** | Mind 35 | +1 Wildcard mantra slot. |
| **Showstopper** | STR 40 | When someone rolls through your attack, you stomp and daze them, and strip their speed buffs. |
| **Champion's Regalia** | STR 25 | After a flourish, your M1s deal +50% posture damage for 10s. |
| **Unwavering Resolve** | STR 40 | Getting parried costs you 33% less posture. |
| **Bulldozer** | STR 25 | Flourishing someone into a wall can break the wall and guardbreaks them. |
| **Spine Cutter** | STR 20 / AGL 25 | Back-hit after a roll cancel triggers a second hit. Can't be parried. |
| **Going Nowhere** | STR 25 / AGL 25 | When someone dodges your attack, they lose momentum and can't sprint. |
| **Matador** | STR 20 / AGL 5 | +20% damage against players in hyperarmor. |
| **Steady Nerves** | STR 15 / AGL 45 | Successful dodges restore posture. |
| **Swift Rebound → Evasive Expert → Risky Moves → Ghost** | AGL 15 / 15 / 25 / 40 | Speed after dodging, an automatic second dodge, and invisibility after a dodge. |
| **Speed Demon** | AGL 25 | Your attacks bleed while you have a speed boost. |
| **Blade Dancer** | AGL 25 | Landing an M1 resets your roll cooldown. |
| **Observation / Safety Dance** | AGL 20 | Bigger dodge windows. |
| **Fast Blade** | AGL 20 | Longer speed boost after a parry (community rating 4.70). |

### B. Post-shrine: Thundercall core
| Talent | Requirement | What it does for you |
|---|---|---|
| **Resolve Crusher → First Interrogation → Second Interrogation** | LTN 65 | Thundercall hits stack Resolve Crusher. Stormseye M1s count. At full stacks the target is **Electrified** and deals **50% less damage and 50% less posture damage to you**. They also refund your ether. **This is the build's centerpiece.** |
| **Authority Intimidation** | LTN 60, Power 10 | Your lightning slows harder. |
| **Surge Path: Unstable Capacitor** | LTN 40 | Shock is replaced by Surge stacks, which Overload into burst damage. |
| **Catalytic Strike** | LTN 50 | Breaking someone's posture Overloads their Surge stacks immediately. |
| **Closed Circuit** | LTN 50 | In a 1v1, an Overload that can't arc to anyone else deals extra damage to its target. |
| **Fried Circuits** | LTN 60 | Overload applies **Sapped** for 5s: their mantra cooldowns go up, and they're shocked when it ends. |
| **Static Link** | LTN 40 / INT 15 | Flourishes and uppercuts tether you to the target. |
| **Jumper Cables** | LTN 40 / FTD 20 | **If you would be knocked while tethered, you steal their health and stay up instead.** |
| **Link Conduction** | LTN 65 | Lightning mantras cost less ether while you're tethered. |
| **Static Blade** | MED 20 / LTN 40 | Blocking, getting parried, and hitting blocks build charges for a speed buff, which feeds Speed Demon. |
| **Grand Skewer** | LTN 60 + Grand Javelin | Grand Javelin carries the target through the air, extending combos. |
| **Will o' Wisp** | 25 attunement + a Wisp mantra | Gives Thunder Wisp its own slot. |
| **Thundercall Unbounded** | LTN 75 + boss kill | Lets you go to 80 LTN for Level 5 mantras. |

### C. Post-shrine: Defense (the "can't die" stack)
| Talent | Requirement | What it does for you |
|---|---|---|
| **Battle Tendency, Braced Collapse, Moving Fortress, Perseverance** | FTD/WLL 15–30 | Prerequisites for Reinforced Armor, and good on their own. |
| **Reinforced Armor** *(Advanced)* | FTD 90 | **Incoming PEN −30%.** Blunts Shattered Katana and Kyrsedge-style 30%-PEN weapons. |
| **Exoskeleton** | FTD 40 | Natural armor that resists 10% physical damage. Stacks with Vesperian Chitin. |
| **To The Finish** | FTD 50 | −10% damage taken below 30% HP. |
| **Mythic Stability** | FTD 85 | You can't be instantly executed while standing. |
| **Defensive Reprisal** | FTD 65 | Getting flourished gives you 10% posture resistance for 20s. |
| **Concussion / Strong Stern** | STR 20 + FTD | Your wallbangs daze longer; theirs daze you half as long. |
| **Padded Armor + Steel Scales** | Power 8 | −10% damage taken once your armor breaks. |
| **Armor Conserver** | Power 8 | Lose 15% less armor per hit. |
| **Disbelief** | WLL 25 | Halves Charm duration on you and shortens illusions. Counters mirror Charm builds and Visionshaper. |
| **Old Habits Die Hard** | WLL 20 | A late block after a failed parry takes 15% less posture damage. |
| **Underdog** | WLL 30 | +2.5–4% damage against higher-HP targets. |
| **Stay of Execution** | CHA or WLL 25 | Executions on you take 20% longer. |

### D. Fill (take them as they appear in your hand)
Wyvern's Claw (+10% damage airborne), Chronostasis (your hits briefly lock their Resonance; very strong in open world), Thresher Claws (if it shows up), Ether Absorption, Replenishing Knockout, Bloodiron Spirit, Callout, Kickstart, Stratoshock.

**Optional:** Electrify + Amplified Rage. Amped gives +20% weapon damage but you take +10% damage for 15s. Take it only if you also run Stormchanter's Raiments, which removes Electrify's self-damage.

---

## 4. Mantras (10 slots + Wisp)

Slots: 3 Combat + 2 from Soulbreaker, 1 Support, 1 Mobility, and 3 Wildcard (base, Soulbreaker and Neuroplasticity).

| Slot | Mantra | Notes |
|---|---|---|
| Combat | **Rising Thunder** (3★) | Launcher; 60 base at L5. Your main finisher. |
| Combat | **Thunder Kick** (1★) | Gains its special Level 5 effect at 80 LTN. Pure thunder damage and a new animation since Jan 2026; new visual effects on Sept 28. |
| Combat | **Jolt Grab** | Grab. **Magnet Spark** variant: no lunge, AoE around you, shorter windup, teleports to the target. |
| Combat | **Rhythm Advance** (Oath) | ~61 damage, **i-frames for the whole move**, AoE. An M1 right after it hits with no windup. |
| Combat | **Ardour Slicer** (Oath) | Long-range projectile with 40% chip. Use it to poke and to punish runners. |
| Wildcard | **Grand Javelin** + Grand Skewer | Carries the target through the air for a combo extension. Keep the base version, not Multiplying Spark. |
| Wildcard | **Electro Carve** | 63 posture damage: your guardbreak, which triggers Catalytic Strike. Hit for −25% damage in Sept 2026, but its posture is untouched. |
| Wildcard | **Tacet Kick** (Oath) | Teleport kick out of Tacet to start a fight. |
| Support | **Lightning Stream** | Base version pulls the target to you. Use it on runners and to set up Jolt Grab. |
| Mobility | **Lightning Cloak** | Mobility. Its swing-speed bonus was cut in Mar 2026, but movement is still strong. |
| Wisp | **Thunder Wisp** | Applies **Sapped** on your uppercuts and flourishes. |

**Deep Gems:**
- **Insignia Gem** (faster windup) on Thunder Kick and Jolt Grab.
- **Bloodless Gem** on Rising Thunder, for healing on your biggest hit.

Get all Thundercall mantras to **Level 5 at 80 LTN** (1,000 notes each).

---

## 5. Weapon — Stormseye

- **Stats:** 19 base, Blunt, MED 3 / LTN 6 scaling, 8 range, 1.0× swing speed. Not enchantable.
- **Drops from:** The Ferryman, Primadon, Elder Primadon, Fury Nautilodaunt, fishing chests, Lodestar bounty, Layer 1, Diluvian Mechanism, or Traan Zakshun's black market.
- **Passives:**
  - *Medallion Shockwave:* every 2nd flourish explodes. With Surge Path it applies a Surge stack. 10s cooldown.
  - *Rosen's Fakeout:* aerial M1s at close range teleport you behind the target.
- **Procs every Static and Electrified talent**, so your M1s build Resolve Crusher and Surge, not only your mantras.
- **Crit:** you circle the target firing 3 shots (0.74× each, 2.22× total) with **i-frames** throughout. The last shot applies a Surge stack. 10s cooldown, 8s with Warmaster's Medallion.

---

## 6. Outfit & equipment (all Pathfinder-obtainable)

| Slot | Item | Effect |
|---|---|---|
| **Outfit** | **Celtorian Tideknight** (Diluvian Mechanism schematic) | 30% physical / 25% elemental / +5% blunt / +10% shadow resistance. *Tidekeeper:* +15% damage, +20% defense, can't be knocked for 10s, 60s cooldown. |
| *Outfit alt* | Black Diver (Nautilodaunt) | 30% physical / 30% elemental / +20% lightning / +20% shadow, 50% ether regen. Used in 25 of the 51 sampled builds. Pick it if your lobbies are full of Thundercall mirrors. |
| Head | **Immortal Helm** (Immortal Guardian) | Immortality: lethal damage leaves you at 1% HP for 2s instead of knocking you. |
| Face | **Necrotic Mask** | Blood Plague: each M1 adds a stack; your crit converts the stacks into temporary health. |
| Arms | **Ossified Simple Pauldrons** | Simple Buff: +7.5% M1 damage. *Alt:* Monastery Champion Robes, which make you take 90% less damage during the first 0.3s of your crit windup. |
| Legs | **Hardened Enforcer Boots** | Enforcer's Technique: **flourishes deal +35% damage**. Combines with Dazing Finisher and the Stormseye shockwave. |
| Torso | **Warmaster's Medallion** | Crit cooldown −20%, or −10% in Chime. Resonance cooldown +20%. |
| Earrings | **Shiva's Pendant Earrings** | Skillful Recovery: +20% posture regen and +20% posture restored on parry. |
| Rings ×4 | **Charged Ring**, **Ring of Pestilence**, **Bloodiron Ring**, **Light Eater Ring** | Charged: Surge Overloads at 5 stacks instead of 6. Pestilence: your weapon applies 50% anti-heal, which shuts down Blood Scourge and regen. Bloodiron: +2% physical armor, armor back on kills. Light Eater: +2% fire/lightning/elemental armor and ether when hit by fire or lightning. *Alt:* Finisher's Ring for PEN on flourishes. |

- **Pips:** take Health on everything you can. 1–2 Physical Armor pips are fine.
- **Equipment enchant:** **Displacement** on one piece. When you're hit there's a 20% chance to get a speed boost, clear all stuns, and gain hyperarmor.
- **Enchant limit:** unenchantable gear now counts toward your enchant slots, so don't plan on stacking enchants.

---

## 7. How to play it

### The three engines
1. **Electrify:** land 4–5 Thundercall hits (Stormseye M1s count) → the target is **Electrified** and deals **half damage and half posture damage to you**. Then play aggressive.
2. **Charm:** any mantra hit Charms them. That gives you +10% damage and them −10% to you. Your next crit gets **+20% (Manipulator)**, and your next flourish **dazes instead of knocking back (Dazing Finisher)**.
3. **Surge:** 5 Surge stacks (with Charged Ring), or a posture break (Catalytic Strike), triggers an Overload → **Sapped**, raising all their mantra cooldowns.

### Core strings
- **Opener:** Ardour on (H, +20% M1 posture damage) → Lightning Stream pull or Magnet Jolt Grab → M1 ×2 → Thunder Kick → M1 → **Stormseye crit** (i-frames; Manipulator if they're Charmed).
- **Burst window:** once ether is ≥ 40%, **Ardour Scream** (+25% damage and +50% posture damage on them for 10s) → Rising Thunder → Grand Javelin (Skewer) → M1 → flourish (Dazing Finisher keeps them close; Enforcer Boots add +35%) → Electro Carve to guardbreak → Catalytic Overload.
- **Anti-turtle:** Electro Carve (63 posture) and M1 chains with Champion's Regalia (+50% M1 posture after a flourish).
- **Anti-roll:** Showstopper, Going Nowhere, and the Stormseye aerial teleport.

### Defensive layers, in the order they trigger
1. Electrified opponent: −50% damage to you.
2. Charm: −10%.
3. Outfit, Exoskeleton (10%) and Chitin (5%) against physical damage. **Reinforced Armor** cuts their PEN by 30%.
4. You lose 25% HP in 3s → **Tidekeeper**: +20% defense, unkillable for 10s.
5. You would be knocked while tethered → **Jumper Cables**: steal their HP and stay up.
6. Lethal hit → **Immortality**: 2s at 1% HP.
7. Escape options: Rhythm Advance and the Stormseye crit both have full i-frames. Tacet → Formless teleports you.

### Open world
- Tacet + Formless to engage on someone who hasn't seen you.
- Rhythm (Heart Reverb) tracks targets through walls and shows HP and posture on anyone who dodges you.
- Chronostasis puts their Resonance on cooldown.
- Blood Scourge (or Soul Infusion's fast grip) to finish.
- Ardour Scream with Soul Infusion reaches 200 studs, so you can combat-tag runners.

### Matchup notes
- **Silentheart:** feint cooldowns +50% and no oath damage since Sept 28. Electrify them early; their M1-heavy pressure gets cut in half.
- **Shattered Katana / high-PEN builds:** Reinforced Armor plus Electrified neutralizes most of their damage.
- **Blindseer:** Tranquil Circle blocks your mantras inside it. Fight on M1s and the Stormseye crit, and step out of the ring to cast.
- **Contractor:** Mythic Stability stops Judgement's instant execute while you're standing. Don't swing into an active Equalizer aura.
- **Visionshaper and other Charm builds:** Disbelief halves their Charm and shortens illusions. Parrying a clone disables its swap for 3s.

---

## 8. Variants

- **Blightsurger instead of Soulbreaker.** The same stats qualify: FTD 90 ≥ 80 combined, LTN 80 ≥ 40.
  - You gain Sovereign Drive (knockdown and daze), Skycrash (ragdoll and daze), Anchor Shock (shuts down their mobility mantras) and Wither on hit. Sovereign Drive's windup was buffed on Sept 28.
  - You lose Ardour Scream, Tacet and Rhythm, and Sovereign State temporarily swaps out your Stormseye.
  - It requires a Titus kill and Hundred Legions reputation.
- **Shattered Katana core:** MED 90 / LTN 75 / FTD 50 / CHA 35 / WLL 25 / STR 25 / AGL 25 / INT 5.
  - It's enchantable (Grim or Erebus), has 30% PEN, and has a strong 2-handed crit.
  - You lose Reinforced Armor and Static Link, and Electrify builds more slowly because Katana M1s don't proc Interrogator.
  - This is roughly the "thundercall medium" community build with Soulbreaker swapped in for the July-nerfed Jetstriker.
- **Chime 1v1 only:** Resonances are disabled there. Warmaster's Medallion still gives −10% crit cooldown.

---

## 9. Honest caveats
- Numbers come from the wiki and builder data as of mid-October 2026. Deepwoken patches often; check the newest `Version History/2026` entries.
- Racial upgrade talents (Hardened Shell) and Thunder Kick's exact Level 5 effect aren't fully documented on the wiki.
- The pre-shrine table assumes the deepwoken.co builder's convention (attunement at 1 before the shrine). Enter it there to confirm.
- Talent cards are random. If something in §3A doesn't show up before your shrine, keep the stat spread anyway: the defense and Thundercall cores carry the build.
