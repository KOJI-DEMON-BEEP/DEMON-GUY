# Deepwoken PvP meta research — October 2026

This is the evidence behind [`../DEEPWOKEN_PVP_BUILD.md`](../DEEPWOKEN_PVP_BUILD.md). It was compiled on 2026-10-13 against patch **3.2.21a** (Oct 1, 2026).

## What was checked

| Source | What was pulled |
|---|---|
| deepwoken.co builder database (server-rendered data) | **1,158 talents, 271 weapons, 267 mantras, 105 outfits, 433 equipment pieces, 55 enchantments, 18 oath entries (17 Oaths + None), 16 races**, plus boons and flaws, with exact requirements and effects |
| deepwoken.co community tier votes | About 1,000 votes per Oath; 38 mantras, 38 talents and 9 weapons with ≥40 votes. Many other pages show no vote data. |
| deepwoken.co community builds | **51 public builds**, mostly tagged PvP / Chime / gank (2024–2026). That covers every Oath and attunement, plus the 24 newest builds on the feed. |
| Fandom wiki (MediaWiki API) | `Version History/2026` (~900 balance lines read), `Version History/2025`, `Verse 3`, all 15 major Oath pages, Resonance, Murmur, Traits, Status Effects, Weapons (damage formula), Shrine of Order, Attributes, Chime of Conflict, Hero Blades, Stormseye, Shattered Katana, Soulthorn, outfit and equipment pages |
| Web search | Third-party tier lists (Playpatch Jul 2026, Earnaldo Aug 2026, Gamestouse Oct 2026), YouTube PvP build titles, wiki forum threads |

## 2026 balance changes that shape PvP

**Systemic**
- Base HP 210 → 220. Exoskeleton's and Fishman's HP bonuses are now innate (May 31).
- **All Oaths give +5% PEN.** This replaced Thresher Claws' all-damage PEN.
- Oath moves get 50% less from damage multipliers (Jan 2).
- Attributes are hard-capped at 100.
- Parry cooldown 1.5s → 1.2s.
- Auto-parry frames 0.55 → 0.3, later 0.45.
- All heavy weapons now have at least 0.1s endlag (Jan 18).
- Unenchantable equipment counts toward your enchant slots.
- Chime: passive regeneration is capped at base resting regen (Sept 28). Resonances are disabled in 1v1.
- A hidden "Chaos" PvP score now affects matchmaking.

**Nerfed (avoid as a core)**
- **Silentheart** (Sept 28): Oath damage removed, feint cooldowns +~50%. Tempo nerfs in June; can't use abilities during parry stun.
- **Jetstriker** (Jul 7): passive Agility bonus removed; Jet Kick no longer snaps to targets and its hitbox shrank.
- **Galebreathe** (Aug 13): After Cut −50%, Pressure Break 25% → 15%, Astral Wind posture −32%, Gale Punch −25%, Wind Gun −15%, higher ether costs, Inhale cooldown.
- **Bloodrend** (Aug 13): Bloodedge, Razor Blitz, Crimson Surge, Vein Tendrils and Bloodfouler all nerfed.
- **Shadowcast:** Eclipse Kick nerfed repeatedly (−20% on Aug 13; reduced on stunned and ragdolled targets). Rising Shadow and Shadow Meteors nerfed.
- **Visionshaper** (Jul): swap windup, Illusory Counter and Mirror Illusion cooldowns up, swapping punished.
- **Starkindred** (Jun): air dash bonus cut, Celestial Assault cooldown 10 → 20s.
- **Arcwarder** (Jan): suit damage buff removed; suit can be interrupted.
- **Resonances:** Payback cooldown up, Paralytic Dust now one hit then wake-up.
- Backstabber reworked; Crypt Blade and Nocturne (PEN 30% → 10%) nerfed.

**Thundercall:** heavily trimmed, but the core is intact.
- Nerfed: Lightning Blade, Lightning Beam, Lightning Clones, Electro Carve (−25% damage, posture unchanged), Lightning Cloak swing speed, Electrify cooldown interactions.
- Untouched or reworked only: **Rising Thunder, Jolt Grab, Grand Javelin, Lightning Stream**. Thunder Kick became pure thunder damage and was reanimated.

**Buffed**
- **Ironsing** (Aug 13): most mantras deal pure Metal damage; Jailer scales with investment.
- **Blightsurger:** progression requirement 15 → 10 (Aug 22); Sovereign Drive windup 0.75 → 0.65s (Sept 28).
- Chainlash (Jun): multi-target and works on monsters.
- Kyrswynter and Soulthorn buffs (Sept).
- Tranquil Circle now counters most Resonances.
- Sclerosteosis now only procs on hits over 10 damage (Sept 28).

## Community tier votes (deepwoken.co, all-time)

**Oaths**

| Oath | Avg /5 | Votes | S / A / B / C / D |
|---|---|---|---|
| **Soulbreaker** | **4.62** | 1148 | 894 / 159 / 46 / 8 / 41 |
| Jetstriker | 4.27 | 1104 | 608 / 313 / 114 / 27 / 42 |
| Fadetrimmer | 4.06 | 1050 | 435 / 386 / 134 / 42 / 53 *(meme votes)* |
| Silentheart | 4.02 | 1108 | 487 / 351 / 152 / 50 / 68 *(mostly before the Sept 28 nerf)* |
| Bladeharper | 3.93 | 1059 | 274 / 543 / 175 / 28 / 39 |
| Starkindred | 3.88 | 1039 | 270 / 495 / 192 / 40 / 42 |
| Contractor | 3.87 | 1034 | 255 / 520 / 185 / 23 / 51 |
| Saintsworn | 3.86 | 997 | 325 / 366 / 189 / 62 / 55 |
| Oathless | 3.76 | 1078 | 249 / 468 / 256 / 54 / 51 |
| Linkstrider | 3.68 | 977 | 331 / 255 / 216 / 92 / 83 |
| Blightsurger | 3.55 | 946 | 177 / 362 / 262 / 93 / 52 |
| Visionshaper | 3.29 | 1055 | 227 / 259 / 287 / 144 / 138 |
| Arcwarder | 2.72 | 1011 | 56 / 139 / 407 / 292 / 117 |
| Blindseer | 2.26 | 1051 | 70 / 96 / 214 / 323 / 348 |

**Top mantras (≥40 votes):**
- Rising Thunder 4.64, Thunder Kick 4.58, Rising Flame 4.56, Fire Blade 4.53, **Jolt Grab 4.51**, Ice Daggers 4.47, Flame Grab 4.40.
- **Grand Javelin 4.29, Lightning Stream 4.28, Electro Carve 4.27**, Ash Slam 4.26, Flare Volley 4.21, Lightning Cloak 4.01.
- Bottom: Lightning Beam 2.20, Lightning Strike 1.44, Bolt Piercer 1.42.

**Top talents (≥40 votes):** Breathing Exercise 4.79, Polished Armor 4.75, Silencer's Song 4.73, Fast Blade 4.70, Fists of Fortitude 4.68, Disbelief 4.48, Ardour Scream 4.45, Padded Armor 4.44, Steel Scales 4.44.

## Patterns across the 51 sampled community PvP builds

- **Outfit:** Black Diver 25 · Ignition Deepdelver 4 · Royal Etrean Guard 3 · Prophet's Cloak 3
- **Murmur:** Ardour 44 of 51
- **Bell:** Blood Scourge 34 · Payback 4 · Smite 2 · Shard Bow 2
- **Oath:** Jetstriker 11 · Chainwarden 5 · Starkindred 5 · Silentheart 5 · Soulbreaker 5 · Visionshaper 4. Most of the Jetstriker and Silentheart builds predate their nerfs.
- **Race:** Etrean, Canor and Vesperian tied at 6 · Khan 5 · Celtor 4
- **Most-taken talents:**
  - Exoskeleton 43 · Thresher Claws 40 · Charismatic Cast 40 · Swift Rebound 40 · Tough Love 39 · Evasive Expert 37
  - Neuroplasticity 34 · Bloodiron Spirit 34 · Moving Fortress / Braced Collapse 33 · Wyvern's Claw 32 · Speed Demon 31 · Spine Cutter 31
  - Showstopper 23 · Champion's Regalia 23 · Reinforced Armor 17
- **Fortitude ≥ 90 (Reinforced Armor):** 14 of 51
- **Closest existing build to Stormbreaker Soul:** ["thundercall medium"](https://deepwoken.co/builder?id=1iTzjW31) (7.7k views): Thundercall + Interrogator + Charm + Static Link / Jumper Cables + Grand Skewer, on Jetstriker with a Shattered Katana. Stormbreaker Soul moves it to Soulbreaker (Jetstriker was nerfed in July) and to Stormseye (whose M1s proc Interrogator), and adds the Fortitude 90 defense layer.

## Why not…?

- **Silentheart:** it was the most-viewed build (56k views), but on Sept 28 it lost its Oath damage and its feint cooldowns went up ~50%.
- **Jetstriker:** its July rework removed the snap-on Jet Kick and the passive Agility bonus.
- **Galebreathe or Bloodrend core:** both had their main PvP tools cut in August.
- **Hero's Blade of Lightning:** very point-efficient (100 LTN only), but 10% PEN, not enchantable, and its M1s don't proc Interrogator the way Stormseye's do.
- **Ironsing:** recently buffed and worth watching. Its mantra pool rates lower and Jailer lost its true-stun.
- **Blightsurger:** a real contender and listed as the alternate Oath. Its kit replaces your weapon during Sovereign State, and it scores 3.55 in votes against Soulbreaker's 4.62.

## Mechanics reference

- **Weapon damage:** Base × (1 + (0.75 × Σ(stat × scaling)/1000 + rings) × (1 + Proficiency × 0.065)). PEN caps at 50% unless you have Million Ton Piercer or Ether Overdrive (Ether Overdrive is mantras-only since Aug 2026).
- **Traits:** 12 points, max 6 each.
  - Vitality: +10 HP per point.
  - Erudition: +25 ether, +5 tempo and +5% tempo gain per point.
  - Proficiency: +6.5% weapon scaling and +2.5% weapon PEN per point.
  - Songchant: +7.5% mantra scaling and +2.5% mantra PEN per point; +2% per point on Oath mantras.
- **Shrine of Order:** Power 8+, no Oath, 10 Knowledge. Averages invested stats; core and weapon stats lose at most 25, attunement stats any amount. Remainder points are refunded.
- **Mantra levels:** L2 / L3 / L4 / L5 need 20 / 40 / 60 / **80** points in the stat.
- **Fortitude:** +0.5 HP per point up to 50, then +0.25 (100 FTD = 37.5 HP). **Strength:** +0.1% melee and mantra PEN per point.
- **Resonances:**
  - Normal: Blood Scourge, Chorus Divide, Crazy Slots, Gravity Field, Jar of Souls, Paralytic Dust, Payback, Portals, Preservation, Resurrection, Run It Back, Sacred Field, Shard Bow, Skeleton Key, Smite, Smokescreen, Wind-Up.
  - Legendary: Dimensional Travel, Teleportation.
  - Corrupted and Drowned versions add power with one downside.
- **Murmurs:** Ardour (+20% M1 posture damage, −15% posture taken; scream debuff), Tacet (invisible outside your bubble), Rhythm (tracking).
- **Origins:** Castaway, Lone Warrior, Deepbound, Voidwalker, Ignition Delver, Authority Ensign, Justicar.

## Sampled community builds
| Views | Build (deepwoken.co id) | Oath | Attunement | Weapon | Outfit | Race | Bell | Updated |
|---|---|---|---|---|---|---|---|---|
| 56230 | [Guide of The Souls V3](https://deepwoken.co/builder?id=QvpOK5qi) | Silentheart | Attunementless | Shattered Katana | Royal Etrean Guard | None | Wind Up | 2026-10-12 |
| 7716 | [thundercall medium](https://deepwoken.co/builder?id=1iTzjW31) | Jetstriker | Thundercall | Shattered Katana | Prophet's Cloak | Etrean | Blood Scourge | 2026-08-24 |
| 6925 | [Contractor Eyes Of Ethiron PvP Build](https://deepwoken.co/builder?id=aIqhcP6a) | Contractor | Galebreathe+Shadowcast | Eyes Of Ethiron | Ignition Deepdelver | Khan | Run It Back | 2026-05-28 |
| 3329 | [the chainwarden pvp build](https://deepwoken.co/builder?id=cYFx12lR) | Chainwarden | Attunementless | — | Black Diver | Vesperian | Blood Scourge | 2026-05-03 |
| 3158 | [Gale x Shadow Pve + PvP Build / Heavy](https://deepwoken.co/builder?id=8CnHIjM5) | Chainwarden | Galebreathe+Shadowcast | Crypt Blade | Ignition Deepdelver | Khan | Payback | 2026-05-05 |
| 3143 | [Wraithclaw PVP](https://deepwoken.co/builder?id=nb4hpi8R) | Jetstriker | Galebreathe | Wraithclaw | Prophet's Cloak | Felinor | Blood Scourge | 2026-06-23 |
| 3113 | [Thunder Med PvP](https://deepwoken.co/builder?id=8cVLXq3G) | Jetstriker | Thundercall | Stormseye | Stormchanter's Raiments | None | Blood Scourge | 2026-05-03 |
| 3080 | [Gale pvp](https://deepwoken.co/builder?id=gGh9zgqK) | Soulbreaker | Galebreathe | — | Black Diver | Etrean | Blood Scourge | 2026-09-02 |
| 2800 | [Beginner Shattered Katana build](https://deepwoken.co/builder?id=1LkrQqJq) | Starkindred | Attunementless | Shattered Katana | Royal Etrean Guard | Khan | Blood Scourge | 2026-06-22 |
| 2709 | [true seraph gale jetstriker](https://deepwoken.co/builder?id=TVuntizG) | Jetstriker | Galebreathe | True Seraph Spear | Black Diver | Celtor | Blood Scourge | 2026-05-05 |
| 2430 | [Red Death Gank Build](https://deepwoken.co/builder?id=9l7qBDrA) | Soulbreaker | Bloodrend+Shadowcast | Red Death (Bleed) | Black Diver | None | Blood Scourge | 2026-09-22 |
| 2392 | [Curved Jetstriker](https://deepwoken.co/builder?id=I2JXpQv1) | Jetstriker | Galebreathe | Curved Blade Of Winds | Prophet's Cloak | Vesperian | Blood Scourge | 2026-08-02 |
| 2236 | [Crypt soulbreaker](https://deepwoken.co/builder?id=GjnXsROu) | Soulbreaker | Shadowcast | Crypt Blade | None | None | None | 2026-05-15 |
| 2236 | [nocturne pvp silentheart!!](https://deepwoken.co/builder?id=Cq8NFizY) | Silentheart | Attunementless | Nocturne | Black Diver | Khan | Blood Scourge | 2026-05-05 |
| 2224 | [Best Dawnwalker Build](https://deepwoken.co/builder?id=eykZhZMB) | Dawnwalker | Attunementless | — | Black Diver | Vesperian | Blood Scourge | 2026-05-02 |
| 2111 | [iron req pvp build](https://deepwoken.co/builder?id=0A8wmWnn) | Chainwarden | Ironsing | Iron Requiem | Black Diver | Chrysid | Blood Scourge | 2026-05-05 |
| 1856 | [Light's Final Toll - PVP - v1](https://deepwoken.co/builder?id=3dsv2zEJ) | Blindseer | Attunementless | Light'S Final Toll | Black Diver | Canor | Smite | 2026-05-05 |
| 1564 | [BOLTCRUSHER(celtor) JETSTRIKER BUILD](https://deepwoken.co/builder?id=tJBdZxvE) | Jetstriker | Thundercall | Boltcrusher | Black Diver | Celtor | Blood Scourge | 2026-05-05 |
| 1483 | [gale thunder pvp](https://deepwoken.co/builder?id=1kGY767T) | Visionshaper | Galebreathe+Thundercall | Hero'S Blade Of Lightning | Ferryman's Coat | Canor | Payback | 2026-05-05 |
| 1458 | [heavy depths gank build](https://deepwoken.co/builder?id=QQrTnmXS) | Jetstriker | Attunementless | — | Black Diver | Canor | Blood Scourge | 2026-07-27 |
| 1421 | [PVP Build](https://deepwoken.co/builder?id=nItbVxrJ) | Starkindred | Attunementless | Flamekeeper Cestus | Black Diver | Celtor | Blood Scourge | 2026-05-05 |
| 1363 | [Bloodrend's Final Soulbreaker](https://deepwoken.co/builder?id=To3c8W8B) | Soulbreaker | Bloodrend | Light'S Final Toll | Navaen Warchief | Vesperian | Payback | 2026-05-05 |
| 1236 | [Shattered Katana + Azure Flames](https://deepwoken.co/builder?id=U2iIrETa) | Visionshaper | Flamecharm | Shattered Katana | Cindergarb | Chrysid | Blood Scourge | 2026-07-11 |
| 1173 | [The Tank](https://deepwoken.co/builder?id=kpKaOX1M) | Oathless | Bloodrend+Frostdraw | Gran Sudaruska | Black Diver | Ganymede | Blood Scourge | 2026-05-02 |
| 917 | [silent heart pvp](https://deepwoken.co/builder?id=2BCrFPwu) | Silentheart | Attunementless | Alloyed Whaling Knife | Black Diver | Adret | Blood Scourge | 2026-05-05 |
| 841 | [pve/pvp build](https://deepwoken.co/builder?id=1CgIyc0s) | Blindseer | Flamecharm+Frostdraw | Gran Sudaruska | Black Diver | Adret | Blood Scourge | 2026-05-05 |
| 784 | [Specter Thundercall jus karita jetstriker build](https://deepwoken.co/builder?id=S7VC5g9r) | Jetstriker | Galebreathe+Thundercall | Anklets Of Alsin | Justicar's Armour | Canor | Portals | 2026-05-02 |
| 700 | [thunder fist](https://deepwoken.co/builder?id=PoTVeWK4) | Oathless | Thundercall | Flamekeeper Cestus | Black Diver | Vesperian | Blood Scourge | 2026-05-04 |
| 690 | [Broken Harper Build](https://deepwoken.co/builder?id=UopSA3yC) | Bladeharper | Attunementless | Shattered Katana | Royal Etrean Guard | Etrean | Blood Scourge | 2026-05-05 |
| 677 | [Shattered Katana uncapped PEN build](https://deepwoken.co/builder?id=nGWeFWuk) | Fadetrimmer | Attunementless | Shattered Katana | Black Diver | Gremor | Blood Scourge | 2026-05-05 |
| 652 | [gale shadow flame ganking build..](https://deepwoken.co/builder?id=0i4eEdEF) | Oathless | Flamecharm+Galebreathe+Shadowcast | — | Black Diver | Felinor | Blood Scourge | 2026-05-05 |
| 557 | [Thundergale PVP](https://deepwoken.co/builder?id=sS0JavSU) | Starkindred | Galebreathe+Thundercall | Stormseye | Justicar's Armour | Felinor | Shard Bow | 2026-05-05 |
| 506 | [Medium Shadowcast Visionshaper](https://deepwoken.co/builder?id=GirzD8It) | Visionshaper | Shadowcast | — | Legion Centurion | Etrean | Blood Scourge | 2026-05-05 |
| 502 | [Eye Of Malic Chime Thing](https://deepwoken.co/builder?id=1MbBcvq1) | Contractor | Bloodrend | — | Black Diver | Adret | Blood Scourge | 2026-05-04 |
| 500 | [The ult katana build](https://deepwoken.co/builder?id=FL8IIEXk) | Starkindred | Attunementless | Shattered Katana | Cloak Of Winds | Gremor | Blood Scourge | 2026-05-02 |
| 487 | [flame thunder blightsurger](https://deepwoken.co/builder?id=YdT0HmtT) | Blightsurger | Flamecharm+Thundercall | Stormseye | None | None | None | 2025-12-06 |
| 482 | [chain warden shadowcast](https://deepwoken.co/builder?id=GQahUFRL) | Chainwarden | Shadowcast | — | Black Diver | None | Blood Scourge | 2026-05-03 |
| 373 | [imperial staff chainwarden](https://deepwoken.co/builder?id=kGYDKOGz) | Chainwarden | Attunementless | Imperial Staff | Black Diver | Canor | Shard Bow | 2026-05-05 |
| 354 | [Azure flames, Shattered katana](https://deepwoken.co/builder?id=YwNCYJMs) | Visionshaper | Flamecharm | Shattered Katana | Flame Worshipper Armor | Chrysid | Blood Scourge | 2026-06-04 |
| 346 | [blightsurger flame thunder](https://deepwoken.co/builder?id=1AcXzJGU) | Blightsurger | Flamecharm+Thundercall | — | None | None | None | 2026-05-03 |
| 341 | [#1 Chime Build](https://deepwoken.co/builder?id=o3pxvR80) | Silentheart | Attunementless | — | Black Diver | Etrean | Blood Scourge | 2026-05-05 |
| 330 | [top godseeker chime build](https://deepwoken.co/builder?id=XuXvjODK) | Arcwarder | Flamecharm+Frostdraw+Thundercall | Kyrstreza | Black Diver | Canor | Gravity Field | 2026-05-01 |
| 326 | [PVP Heavy Jetstriker](https://deepwoken.co/builder?id=i6mk6aM5) | Jetstriker | Shadowcast+Thundercall | Alloyed Halberd | Ignition Deepdelver | Vesperian | Blood Scourge | 2026-05-04 |
| 276 | [Bloodbane Chime PvP](https://deepwoken.co/builder?id=NaLYvK6R) | Bladeharper | Bloodrend | Bloodbane | Familiar Heretic's Armor | None | Smite | 2026-07-04 |
| 267 | [pvp-thundercall](https://deepwoken.co/builder?id=SP8RDzz5) | Starkindred | Thundercall | Shattered Katana | Black Diver | Celtor | Blood Scourge | 2026-04-28 |
| 254 | [#1 Chime Build - Heavy Variation](https://deepwoken.co/builder?id=q7Z9QwzJ) | Silentheart | Attunementless | — | Black Diver | Etrean | Blood Scourge | 2026-05-03 |
| 253 | [Blightsurger Wraithclaw Build](https://deepwoken.co/builder?id=UZk5b723) | Blightsurger | Galebreathe+Thundercall | Wraithclaw | None | None | None | 2026-05-05 |
| 229 | [chime build](https://deepwoken.co/builder?id=0xRrRcqD) | Blindseer | Flamecharm | Light'S Final Toll | Black Diver | Khan | Blood Scourge | 2026-04-03 |
| 157 | [Attless, Medium, Soulbreaker, Ganks](https://deepwoken.co/builder?id=DUdj87zC) | Soulbreaker | Attunementless | Shattered Katana | None | None | Blood Scourge | 2026-07-01 |
| 131 | [PvP?](https://deepwoken.co/builder?id=6agXuJW4) | Jetstriker | Galebreathe | Curved Blade Of Winds | Tempestmaker's Threads | None | Payback | 2026-05-05 |
| 27 | [whatever the hell that is](https://deepwoken.co/builder?id=zvmcRNc8) | Jetstriker | Thundercall | Central Dirk | Ignition Deepdelver | None | Dimensional Travel | 2026-02-10 |

## Source links

- Deepwoken Wiki — [Version History/2026](https://deepwoken.fandom.com/wiki/Version_History/2026), [Version History/2025](https://deepwoken.fandom.com/wiki/Version_History/2025), [Verse 3](https://deepwoken.fandom.com/wiki/Verse_3), [Oaths](https://deepwoken.fandom.com/wiki/Oaths), [Oath: Soulbreaker](https://deepwoken.fandom.com/wiki/Oath:_Soulbreaker), [Oath: Blightsurger](https://deepwoken.fandom.com/wiki/Oath:_Blightsurger), [Resonance](https://deepwoken.fandom.com/wiki/Resonance), [Traits](https://deepwoken.fandom.com/wiki/Traits), [Weapons](https://deepwoken.fandom.com/wiki/Weapons), [Stormseye](https://deepwoken.fandom.com/wiki/Stormseye), [Celtorian Tideknight](https://deepwoken.fandom.com/wiki/Celtorian_Tideknight), [Chime of Conflict](https://deepwoken.fandom.com/wiki/Chime_of_Conflict), [Shrine of Order](https://deepwoken.fandom.com/wiki/Deep_Shrines/Shrine_of_Order)
- Deepwoken Builder — [Wiki](https://deepwoken.co/wiki), [Oath: Soulbreaker](https://deepwoken.co/wiki/oath/Soulbreaker), [Builds feed](https://deepwoken.co/feed)
- Third-party (lower confidence) — [Playpatch tier list](https://playpatch.org/roblox/deepwoken/tier-list/), [Earnaldo weapon tier list](https://earnaldo.com/blog/deepwoken-tier-list-2026), [Gamestouse oath tier list](https://gamestouse.com/tier-list/deepwoken-oath-tier-list/), [Robloxdatabase tier list](https://robloxdatabase.com/guides/deepwoken-tier-list/)
