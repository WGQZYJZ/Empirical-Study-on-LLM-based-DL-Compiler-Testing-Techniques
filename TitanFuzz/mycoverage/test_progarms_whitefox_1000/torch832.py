import torch
from torch import nn


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 3, 1)
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = v2 * 3
        v4 = torch.relu(v3)
        v5 = v4 + 3
        v6 = torch.relu(v5)
        v7 = v6 * 3
        v8 = v7 + 3
        v9 = v3.repeat(1, 3)
        v10 = v6.repeat(1, 3, 1, 1)
        v11 = v2.repeat(1, 3, 1, 1)
        v12 = v11.permute(0, 1, 3, 2)
        v13 = v10.permute(0, 2, 1, 3)
        v14 = v7 - 3
        v15 = torch.relu(v14)
        v16 = v15 - 3
        v17 = torch.relu(v16)
        v18 = v17 - 3
        v19 = torch.relu(v18)
        v20 = v19 - 3
        v21 = v20 - 3
        v22 = v14.repeat(1, 3)
        v23 = v16.repeat(1, 3)
        v24 = v12.repeat(1, 1, 1, 3)
        v25 = v13.repeat(1, 1, 1, 3)
        v26 = v24.permute(0, 3, 1, 2)
        v27 = v15.repeat(1, 3, 1, 1)
        v28 = v25.permute(0, 3, 1, 2)
        v29 = v17.repeat(1, 3, 1, 1)
        v30 = v26.repeat(1, 1, 1, 3)
        v31 = v27.permute(0, 3, 1, 2)
        v32 = v18.repeat(1, 3, 1, 1)
        v33 = v28.repeat(1, 1, 1, 3)
        v34 = v19.repeat(1, 3, 1, 1)
        v35 = v29.repeat(1, 1, 1, 3)
        v36 = v20.repeat(1, 3, 1, 1)
        v37 = v30.repeat(2, 1, 1, 1)
        v38 = v2.repeat(1, 3, 1, 1)
        v39 = v21.repeat(3, 1)
        v40 = v22.chunk(3, dim=1)
        v41 = v23.chunk(3)
        v42 = v24.chunk(3)
        v43 = v25.chunk(3)
        v44 = torch.cat(v40, dim=2)
        v45 = torch.cat(v41, dim=0)
        v46 = torch.cat(v42, dim=1)
        v47 = torch.cat(v43, dim=3)
        v48 = v31.permute(0, 2, 3, 1)
        v49 = v30.permute(0, 3, 2, 1)
        v50 = v32.permute(0, 3, 2, 1)
        v51 = v35.permute(0, 1, 3, 2)
        v52 = v34.permute(0, 1, 3, 2)
        v53 = v33.permute(0, 1, 3, 2)
        v54 = v36.chunks(3, dim=1)
        v55 = v29.permute(0, 1, 3, 2)
        v56 = v28.permute(0, 3, 2, 1)
        v57 = v27.permute(0, 3, 2, 1)
        v58 = v37.permute(0, 1, 3, 2)
        v59 = v58.permute(0, 2, 1, 3)
        v60 = v53.permute(0, 3, 1, 2)
        v61 = v55.permute(0, 1, 3, 2)
        v62 = v57.permute(0, 1, 3, 2)
        v63 = v54[0].permute(0, 3, 1, 2)
        v64 = v39[2].chunk(1, dim=1)
        v65 = v39[2].chunk(1, dim=1)
        v66 = v39[2].chunk(1, dim=1)
        v67 = v57.permute(0, 2, 3, 1)
        v68 = v51.permute(0, 2, 3, 1)
        v69 = v64[1].permute(0, 1, 3, 2)
        v70 = v59.permute(0, 2, 3, 1)
        v71 = v56.permute(0, 2, 3, 1)
        v72 = v66[0].permute(0, 1, 3, 2)
        v73 = v67.repeat(1, 3, 1, 1)
        v74 = v69.repeat(1, 3, 1, 1)
        v75 = v70.repeat(1, 3, 1, 1)
        v76 = v72.repeat(1, 3, 1, 1)
        v77 = v71.repeat(1, 3, 1, 1)
        v78 = v61.permute(0, 2, 3, 1)
        v79 = torch.cat(v65, dim=0)
        v80 = torch.cat(v63, dim=2)
        v81 = v50.permute(0, 2, 3, 1)
        v82 = v79.repeat(3, 1)
        v83 = v49.repeat(1, 3, 1)
        v84 = v76.permute(0, 2, 1, 3)
        v85 = v83.chunk(3, dim=2)
        v86 = v77.permute(0, 2, 3, 1)
        v87 = v84.repeat(1, 1, 3, 3)
        v88 = v73.permute(0, 2, 3, 1)
        v89 = v81.permute(0, 2, 3, 1)
        v90 = v82.chunk(12, dim=1)
        v91 = torch.cat(v80, dim=1)
        v92 = torch.cat(v85, dim=1)
        v93 = torch.cat(v90, dim=2)
        v94 = v78.permute(0, 2, 3, 1)
        v95 = torch.cat(v89, dim=1)
        v96 = v95.repeat(1, 1, 3, 3)
        v97 = v95.permute(0, 2, 1, 3)
        v98 = v92.permute(0, 3, 1, 2)
        v99 = torch.cat(v88, dim=1)
        v100 = v82.permute(1, 0)
        v101 = v75.permute(0, 2, 1, 3)
        v102 = v94.repeat(1, 3, 1, 1)
        v103 = v90.permute(1, 0)
        v104 = v74.chunks(3, dim=1)
        v105 = torch.cat(v104, dim=2)
        v106 = v82.permute(1, 2, 3, 0)
        v107 = v103.permute(1, 0)
        v108 = v87.permute(0, 3, 1, 2)
        v109 = v101.permute(0, 2, 3, 1)
        v110 = v108.repeat(3, 1, 1, 1)
        v111 = v101.permute(0, 3, 1, 2)
        v112 = v93.permute(1, 0)
        v113 = v96.permute(0, 3, 1, 2)
        v114 = v100.permute(1, 0)
        v115 = torch.cat(v98, dim=0)
        v116 = v103.max(dim=0)[0]
        v117 = v112.max(dim=0)[0]
        v118 = v114.min(dim=0)[0]
        v119 = v82.permute(1, 0)
        v120 = v82.permute(1, 0)
        v121 = v110.max(dim=0)[0]
        v122 = v91 + v86
        v123 = v111.max(dim=0)[0]
        v124 = v111.max(dim=0)[0]
        v125 = v113.max(dim=0)[0]
        v126 = v117.max(dim=0)[0]
        v127 = v119.min(dim=0)[0]
        v128 = v119.min(dim=0)[0]
        v129 = v105.permute(0, 2, 1, 3)
        v130 = v115.max(dim=0)[0]
        v131 = torch.cat(v91, dim=0)
        v132 = v103.permute(1, 0, 2)
        v133 = torch.cat(v107, dim=0)
        v134 = v82.permute(1, 0)
        v135 = v123.min(dim=0)[0]
        v136 = torch.cat(v115, dim=0)
        v137 = torch.cat(v129, dim=0)
        v138 = torch.cat(v132, dim=0)
        v139 = v133.permute(1, 2, 0)
        v140 = v122 + v74.permute(1, 0, 2)
        v141 = v126.max(dim=0)[0]
        v142 = v134.permute(1, 0, 2)
        v143 = torch.cat(v131, dim=0)
        v144 = v139.permute(1, 2, 0)
        v145 = torch.cat(v127, dim=0)
        v146 = v105.permute(0, 2, 3, 1)
        v147 = torch.cat(v138, dim=0)
        v148 = v82.permute(0, 2, 3, 1)
        v149 = v123.max(dim=0)[0]
        v150 = v97.permute(0, 3, 2, 1)
        v151 = v97.permute(0, 3, 2, 1)
        v152 = v134.permute(1, 0, 2)
        v153 = torch.cat(v148, dim=0)
        v154 = torch.cat(v136, dim=0)
        v155 = v142.permute(1, 2, 0)
        v156 = torch.cat(v121, dim=0)
        v157 = torch.cat(v130, dim=0)
        v158 = torch.cat(v147, dim=0)
        v159 = v149.min(dim=0)[0]
        v160 = v137.permute(1, 0, 2)
        v161 = v156.max(dim=0)[0]
        v162 = torch.cat(v154, dim=0)
        v163 = torch.cat(v144, dim=0)
        v164 = torch.cat(v140, dim=0)
        v165 = v150.permute(0, 2, 3, 1)
        v166 = torch.cat(v125, dim=0)
        v167 = torch.cat(v152, dim=0)
        v168 = torch.cat(v141, dim=0)
        v169 = v99.permute(1, 0, 2)
        v170 = v99.permute(1, 2, 0)
        v171 = v87.permute(0, 2, 3, 1)
        v172 = torch.cat(v160, dim=0)
        v173 = v96.permute(0, 2, 1, 3)
        v174 = v163[2].chunk(1)
        v175 = torch.cat(v162, dim=0)
        v176 = v102.permute(1, 2, 0)
        v177 = v168.permute(1, 0, 2)
        v178 = torch.cat(v157, dim=0)
        v179 = v115.min(dim=0)[0]
        v180 = torch.cat(v158, dim=0)
        v181 = torch.cat(v164, dim=0)
        v182 = torch.cat(v170, dim=0)
        v183 = v171.permute(1, 2, 0)
        v184 = v143.permute(1, 0, 2)
        v185 = v161.min(dim=0)[0]
        v186 = v172.permute(1, 0, 2)
        v187 = v168.permute(1, 2, 0)
        v188 = torch.cat(v175, dim=0)
        v189 = v177.permute(1, 0, 2)
        v190 = torch.cat(v165, dim=0)
        v191 = torch.cat(v180, dim=0)
        v192 = torch.cat(v166, dim=0)
        v193 = torch.cat(v184, dim=0)
        v194 = v179.min(dim=0)[0]
        v195 = torch.cat(v178, dim=0)
        v196 = v181.permute(1, 0, 2)
        v197 = torch.cat(v188, dim=0)
        v198 = v135 + v145
        v199 = v182.permute(1, 0, 2)
        v200 = torch.cat(v151, dim=0)
        v201 = v174[0].permute(0, 1, 3, 2)
        v202 = torch.cat(v187, dim=0)
        v203 = torch.cat(v185, dim=0)
        v204 = v173.permute(1, 0, 2)
        v205 = torch.cat(v176, dim=0)
        v206 = torch.cat(v195, dim=0)
        v207 = v167.permute(1, 2, 0)
        v208 = v184.permute(1, 2, 0)
        v209 = v200.permute(1, 2, 0)
        v210 = v193.permute(1, 2, 0)
        v211 = torch.cat(v186, dim=0)
        v212 = torch.cat(v189, dim=0)
        v213 = torch.cat(v190, dim=0)
        v214 = v198.permute(1, 0, 2)
        v215 = torch.cat(v198, dim=0)
        v216 = torch.cat(v183, dim=0)
        v217 = torch.cat(v209, dim=0)
        v218 = torch.cat(v205, dim=0)
        v219 = v216.permute(1, 0, 2)
        v220 = v219.permute(1, 2, 0)
        v221 = v218.permute(1, 0, 2)
        v222 = v212.permute(1, 2, 0)
        v223 = v207.permute(1, 2, 0)
        v224 = v220.permute(1, 2, 0)
        v225 = torch.cat(v217, dim=0)
        v226 = v224.permute(1, 0, 2)
        v227 = torch.cat(v214, dim=0)
        v228 = torch.cat(v215, dim=0)
        v229 = torch.cat(v211, dim=0)
        v230 = torch.cat(v201, dim=0)
        v231 = torch.cat(v199, dim=0)
        v232 = torch.cat(v191, dim=0)
        v233 = torch.cat(v210, dim=0)
        v234 = torch.cat(v222, dim=0)
        v235 = torch.cat(v226, dim=0)
        v236 = torch.cat(v229, dim=0)
        v237 = torch.cat(v194, v203, dim=2)
        v238 = v237.permute(2, 0, 1)
        v239 = torch.cat(v227, dim=0)
        v240 = torch.cat(v223, dim=0)
        v241 = v233.permute(1, 0, 2)
        v242 = torch.cat(v206, dim=0)
        v243 = v230.permute(1, 0, 2)
        v244 = torch.cat(v196, dim=0)
        v245 = v239.permute(1, 2, 0)
        v246 = torch.cat(v225, dim=0)
        v247 = torch.cat(v238, dim=0)
        v248 = torch.cat(v242, dim=0)
        v249 = torch.cat(v204, dim=0)
        v250 = v235.permute(1, 2, 0)
        v251 = torch.cat(v234, dim=0)
        v252 = v245.repeat(1, 3, 1, 1)
        v253 = v221.permute(1, 2, 0)
        v254 = torch.cat(v240, dim=0)
        v255 = v250.permute(1, 2, 0)
        v256 = torch.cat(v232, dim=0)
        v257 = v248.permute(1, 0, 2)
        v258 = torch.cat(v236, dim=0)
        v259 = v244.permute(1, 2, 0)
        v260 = v246.repeat(1, 3, 1, 1)
        v261 = v243.permute(1, 2, 0)
        v262 = torch.cat(v241, dim=0)
        v263 = torch.cat(v253, dim=0)
        v264 = v256.repeat(1, 3, 1, 1)
        v265 = torch.cat(v252, dim=0)
        v266 = torch.cat(v255, dim=0)
        v267 = torch.cat(v249, dim=0)
        v268 = torch.cat(v258, dim=0)
        v269 = torch.cat(v257, dim=0)
        v270 = torch.cat(v251, dim=0)
        v271 = torch.cat(v261, dim=0)
        v272 = v267.permu
m = Model()