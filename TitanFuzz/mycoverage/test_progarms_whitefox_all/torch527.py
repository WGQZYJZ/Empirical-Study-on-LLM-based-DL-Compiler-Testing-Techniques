import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 7, 2, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
    def forward(self, x1, x2):
        v1 = self.conv(x2)
        v2 = self.conv_transpose(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2 * v2
        v5 = v4 * 0.044715
        v6 = v2 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = torch.tanh(v5)
        v11 = v8 * v10
        v12 = v4 * 0.8820041700000384
        v13 = v3 + v12
        v14 = v12 * 0.5748223191636137
        v15 = torch.tanh(v4)
        v16 = v15 + 1
        v17 = v14 * v16
        v18 = v2 + v13
        v19 = v9 * v11
        v20 = v6 + v11
        v21 = v20 * 0.8549265894198312
        v22 = torch.tanh(v3)
        v23 = v22 + 1
        v24 = v2 * v23
        v25 = v24 * v23
        v26 = v23 + v17
        v27 = v22 + v26
        v28 = v27 * 0.9761075802224983
        v29 = torch.tanh(v24)
        v30 = v28 * v29
        v31 = v23 * 0.6774068465664719
        v32 = v23 * v30
        v33 = v31 * v25
        v34 = v17 + v33
        v35 = v34 * 0.5599209383261169
        v36 = v27 * 0.9659086879763777
        v37 = v36 * v11
        v38 = v17 + v25
        v39 = v19 * 0.589764085850388
        v40 = v39 * v19
        v41 = v10 * v34
        v42 = v37 + v41
        v43 = v42 * 0.7826491610623416
        v44 = v35 * v30
        v45 = v29 * v38
        v46 = v44 + v45
        v47 = v46 * 0.8623811751281535
        v48 = v47 * v23
        v49 = v48 * v23
        v50 = v25 + v19
        v51 = v49 + v30
        v52 = v51 * 0.6696856642352267
        v53 = v23 + v25
        v54 = v50 * 0.902221716980452
        v55 = v37 + v38
        v56 = v55 * 0.5541535460167811
        v57 = v42 + v35
        v58 = v34 * 0.7024204744759221
        v59 = v58 * v30
        v60 = v37 + v51
        v61 = v19 + v49
        v62 = v61 * 0.5761678072124059
        v63 = v54 * v52
        v64 = v56 + v62
        v65 = v63 + v64
        v66 = v60 * 0.7358627291500292
        v67 = v50 * 0.6111592322158797
        v68 = v66 * v65
        v69 = v40 + v62
        v70 = v65 + v67
        v71 = v68 * v70
        v72 = v60 + v69
        v73 = v64 + v68
        v74 = v71 * 0.8903412902382142
        v75 = v56 + v73
        v76 = v50 + v72
        v77 = v71 + v76
        v78 = v73 + v77
        v79 = v77 + v78
        v80 = v75 + v79
        v81 = v79 * 0.7068578571843806
        v82 = v54 * v81
        v83 = v67 + v81
        v84 = v82 + v83
        v85 = v80 * 0.5216865402134983
        x0 = v61 + v82`
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 2, 8, 4)
