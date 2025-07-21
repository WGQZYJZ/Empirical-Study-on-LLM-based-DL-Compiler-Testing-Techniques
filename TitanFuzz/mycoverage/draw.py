# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

program_counts = [10, 100, 1000, 10000]
technologies = {
    "WhiteFox": {
        "mean": [4.62, 4.87, 5.04, 4.94],
        "variance": [3.56, 5.49, 4.57, 4.83]
    },
    "TitanFuzz": {
        "mean": [4.33, 2.90, 2.12, 2.13],
        "variance": [4.09, 4.70, 2.45, 2.45]
    }
}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(hspace=0.4)

for tech in technologies:
    ax1.plot(program_counts, technologies[tech]["mean"], 
             marker='o', label=tech)
ax1.set_title('代码风格评分均值对比')
ax1.set_xlabel('程序数目')
ax1.set_ylabel('均值 (满分10分)')
ax1.set_xscale('log')
ax1.grid(True, which="both", ls="--")
ax1.legend()
ax1.set_xticks(program_counts)
ax1.set_xticklabels(program_counts)

for tech in technologies:
    ax2.plot(program_counts, technologies[tech]["variance"], 
             marker='s', linestyle='--', label=tech)
ax2.set_title('代码风格评分方差对比')
ax2.set_xlabel('程序数目')
ax2.set_ylabel('方差')
ax2.set_xscale('log')
ax2.grid(True, which="both", ls="--")
ax2.legend()
ax2.set_xticks(program_counts)
ax2.set_xticklabels(program_counts)

plt.tight_layout()
plt.show()
plt.savefig('code_style_scores.png', dpi=300, bbox_inches='tight')  
print("图表已保存为 code_style_scores.png")