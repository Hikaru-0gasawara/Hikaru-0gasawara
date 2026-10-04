<!--
  Every panel on this profile is an SVG drawn by gen/ (Python, no dependencies)
  and redrawn daily by .github/workflows/profile.yml with live numbers from the GitHub API.
  ↑ ↑ ↓ ↓ ← → ← → B A  — on the portfolio that's worth 30 lives.
-->

<p align="center">
  <a href="https://hikaru-0gasawara.github.io/Portifolio/"><img src="assets/banner.svg" width="100%" alt="HIKARU OGASAWARA — 小笠原 光 · Junior Security Analyst · São Paulo, Brazil. From pin to server: pin, register, firmware, MQTT/TLS, network, firewall, server, SIEM."></a>
</p>

<p align="center"><a href="https://hikaru-0gasawara.github.io/Portifolio/"><img src="assets/button-portfolio.svg" width="33.333%" alt="Portfolio"></a><a href="https://www.linkedin.com/in/hikaru-ogasawara"><img src="assets/button-linkedin.svg" width="33.333%" alt="LinkedIn"></a><a href="mailto:hogasawara2311@outlook.com"><img src="assets/button-email.svg" width="33.333%" alt="E-mail"></a></p>

### `$ whoami` &nbsp;·&nbsp; about

<p align="center">
  <img src="assets/fetch.svg" width="100%" alt="ASCII portrait next to a neofetch-style card: OS Windows 11, Pop!_OS and Kali Linux; São Paulo, Brazil; Junior Security Analyst; uptime counted from birth; Computer Engineering at Ibmec (2023–2027); Python, Java, C/C++ and SQL; C++ and MicroPython for firmware; Portuguese, English, Japanese and Spanish; SIEM, Kali Linux, IPFire and iptables; Proxmox, AD/DC, DNS, DHCP and Linux; ESP32, Arduino UNO and Raspberry Pi Pico; Ycare and Kochi Kenjinkai; GitHub numbers.">
</p>

I started with hardware: connecting a sensor, reading a register, understanding why a signal came in distorted. Then came infrastructure, and then security. I like the boundary where physical becomes logical and where logic can be attacked. Today I'm a **Junior Security Analyst**.

I learn by doing: assemble, test, measure, break and rebuild until it works properly, understanding why before accepting how. I study Computer Engineering at Ibmec and, away from the keyboard, I'm vice president of Ycare, a volunteer organization that delivers food and hygiene baskets to a community on the second Saturday of every month.

```diff
@@ bio.md · d15ca1c · fix(bio): take off shoes @@
- I prefer working with shoes on: layer after layer between me and the machine.
+ I prefer working barefoot: bare metal, nothing between me and the machine.
```

### `$ inventory --equipped` &nbsp;·&nbsp; stack

<p align="center">
  <img src="assets/loadout.svg" width="100%" alt="Equipped: C/C++, Python, SQL, embedded systems, Kali Linux, SIEM, Git and Java. Backpack: ESP32, Arduino UNO, Raspberry Pi Pico, MicroPython, LogiSim, I²C, UART, PWM, MQTT over TLS, Proxmox, AD/DC, IPFire, iptables, ufw, DNS/DHCP, Linux, TypeScript with React, HTML/CSS, Jupyter, NumPy, pandas, Power BI, AWS Lambda, Vitest, Playwright, JUnit and Postman.">
</p>

### `$ ls ~/projects` &nbsp;·&nbsp; projects

<p align="center"><a href="https://hikaru-0gasawara.github.io/Portifolio/"><img src="assets/project-infra-lab.svg" width="50%" alt="Infrastructure lab: AD/DC, IPFire firewall and SIEM built from scratch, virtualized on Proxmox, checked with Kali Linux."></a><a href="https://github.com/Hikaru-0gasawara/IoT-PoolHardWareTest"><img src="assets/project-aquasense.svg" width="50%" alt="AquaSense IoT: ESP32 firmware for 7 water parameters, MQTT/TLS, React dashboard and an Alexa skill."></a></p>
<p align="center"><a href="https://github.com/Hikaru-0gasawara/IoT-SafeSistem"><img src="assets/project-cofre.svg" width="50%" alt="Electronic safe: the same safe ported to Arduino UNO, Raspberry Pi Pico and ESP32."></a><a href="https://github.com/0tavio-Pires/Projeto_Back-End"><img src="assets/project-cptm.svg" width="50%" alt="CPTM assets: Spring Boot REST API with 14 endpoints for trains, stations and lines."></a></p>
<p align="center">
  <a href="https://hikaru-0gasawara.github.io/Portifolio/"><img src="assets/project-portfolio.svg" width="100%" alt="Portifolio: an explorable pixel-art room with a 3D TV in hand-written WebGL, minigames, 51 achievements and a recruiter mode. PT, EN and 日本語."></a>
</p>

### `$ gh status` &nbsp;·&nbsp; github

<p align="center"><img src="assets/stats.svg" width="50%" alt="GitHub stats: contributions, commits, pull requests, issues, stars, followers and level."><img src="assets/langs.svg" width="50%" alt="Most used languages across public repositories."></p>
<p align="center"><img src="assets/streak.svg" width="50%" alt="Contribution streak: total, current streak and longest streak."><img src="assets/trophies.svg" width="50%" alt="Trophies from C to SSS for commits, repositories, pull requests, contributions, languages, account age, stars and followers."></p>
<p align="center">
  <img src="assets/activity.svg" width="100%" alt="Activity graph: contributions per day over the last 31 days.">
</p>
<p align="center">
  <img src="assets/snake.svg" width="100%" alt="A snake eating the contribution graph of the last 12 months.">
</p>

### `$ ping hikaru` &nbsp;·&nbsp; contact

Want to talk security, infrastructure or embedded systems? Reach me on [LinkedIn](https://www.linkedin.com/in/hikaru-ogasawara) or at [hogasawara2311@outlook.com](mailto:hogasawara2311@outlook.com). The [portfolio](https://hikaru-0gasawara.github.io/Portifolio/) has my résumé in PT, EN and 日本語, plus a recruiter mode for when you're in a hurry.

<p align="center">
  <a href="https://hikaru-0gasawara.github.io/Portifolio/"><img src="assets/footer.svg" width="100%" alt="CONTINUE? Thanks for playing · ありがとう."></a>
</p>

<details>
<summary><code>$ cat HOW_IT_WORKS.md</code></summary>

<br>

- Nothing here depends on an outside service to load: every panel is an SVG generated by `python -m gen` (standard library only) and served straight from this repository.
- `.github/workflows/profile.yml` runs daily: [Platane/snk](https://github.com/Platane/snk) draws the snake, the generator pulls the numbers from GitHub's GraphQL API, and the bot commits `assets/`.
- Animations are CSS inside the SVGs (GitHub shows images through `<img>`, which runs CSS but never JavaScript). JetBrains Mono and DotGothic16 are embedded, subset to just the characters used.
- The link buttons and the side-by-side cards are separate images placed edge to edge; the gaps are drawn inside each SVG, so every row lines up with the full-width panels.
- The portrait is my photo turned into coloured ASCII by `gen/tools/portrait.py`; the palette, icons and inventory come from the [portfolio](https://github.com/Hikaru-0gasawara/Portifolio).
- To change texts, projects or the inventory: `gen/config.json`. To iterate without spending API calls: `python -m gen --cache data.json`.

</details>
