import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(128, 128, 3, stride=1, padding=1)
        self.conv_1 = torch.nn.Conv2d(128, 64, 3, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
    def forward(self, x6):
        v0 = x6 * 0.02544217687072754
        v1 = self.conv(v0)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v11 = v10 + 0.41614683678627014
        v12 = self.conv_1(v11)
        v13 = v12 * 0.5
        v14 = v12 * v12
        v15 = v14 * v12
        v16 = v15 * 0.044715
        v17 = v12 + v16
        v18 = v17 * 0.7978845608028654
        v19 = torch.tanh(v18)
        v20 = v19 + 1
        v21 = v13 * v20
        v22 = v21 * 0.3178876478954316
        v23 = self.conv_2(v22)
        v24 = v23 * 0.5
        v25 = v23 * v23
        v26 = v25 * v23
        v27 = v26 * 0.044715
        v28 = v23 + v27
        v29 = v28 * 0.7978845608028654
        v30 = torch.tanh(v29)
        v31 = v30 + 1
        v32 = v24 * v31
        v33 = v1 + v10
        v34 = v32 * v33
        v35 = v34 * 0.5
        v36 = v34 * v34
        v37 = v36 * v34
        v38 = v37 * 0.044715
        v39 = v34 + v38
        v40 = v39 * 0.7978845608028654
        v41 = torch.tanh(v40)
        v42 = v41 + 1
        v43 = v35 * v42
        v44 = v11 + v22
        v45 = v43 * v44
        v46 = v45 * 0.5
        v47 = v45 * v45
        v48 = v47 * v45
        v49 = v48 * 0.044715
        v50 = v45 + v49
        v51 = v50 * 0.7978845608028654
        v52 = torch.tanh(v51)
        v53 = v52 + 1
        v54 = v46 * v53
        v55 = v2 + v31
        v56 = v54 * v55
        v57 = v56 * 0.5
        v58 = v56 * v56
        v59 = v58 * v56
        v60 = v59 * 0.044715
        v61 = v56 + v60
        v62 = v61 * 0.7978845608028654
        v63 = torch.tanh(v62)
        v64 = v63 + 1
        v65 = v57 * v64
        v66 = v12 + v24)
        v67 = v65 * 0.5
        v68 = v65 * v65
        v69 = v68 * v65
        v70 = v69 * 0.044715
        v71 = v65 + v70
        v72 = v71 * 0.7978845608028654
        v73 = torch.tanh(v72)
        v74 = v73 + 1
        v75 = v66 * v74
        v76 = v28 + v57
        v77 = v75 * v76
        v78 = v77 * 0.5
        v79 = v77 * v77
        v80 = v79 * v77
        v81 = v80 * 0.044715
        v82 = v77 + v81
        v83 = v82 * 0.7978845608028654
        v84 = torch.tanh(v83)
        v85 = v84 + 1
        v86 = v78 * v85
        v87 = v61 + v86
        v88 = v87 * 0.5
        v89 = v87 * v87
        v90 = v89 * v87
        v91 = v90 * 0.044715
        v92 = v87 + v91
        v93 = v92 * 0.7978845608028654
        v94 = torch.tanh(v93)
        v95 = v94 + 1
        v96 = v88 * v95
        v97 = v8 + v47)
        v98 = v97 * 0.5
        v99 = v97 * v97
        v100 = v99 * v97
        v101 = v100 * 0.044715
        v102 = v97 + v101
        v103 = v102 * 0.7978845608028654
        v104 = torch.tanh(v103)
        v105 = v104 + 1
        v106 = v98 * v105
        return v106

m = Model()
# Inputs to the model
x6 = torch.randn(1, 128, 16, 16)
