import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Model(torch.nn.Module):

    def __init__(self, min_value=0.4907, max_value=0.425):
        super().__init__()
        self.conv2d_12 = torch.nn.Conv2d(16, 1, 7, stride=1, padding=0)
        self.conv2d_11 = torch.nn.Conv2d(64, 2048, 1, stride=1, padding=0)
        self.conv2d_10 = torch.nn.Conv2d(512, 1024, 1, stride=1, padding=0)
        self.max = torch.nn.MaxPool2d(3, stride=2, padding=0, ceil_mode=False)
        self.relu = torch.nn.ReLU(True)
        self.conv2d_6 = torch.nn.Conv2d(8, 64, 7, stride=2, padding=3)
        self.conv2d_4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(2048, 512, 1, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv2d_12(x1)
        v2 = self.conv2d_11(v1)
        v3 = v2.data
        v4 = v3.data.data
        v5 = self.conv2d_10(v4)
        v6 = v5.data
        v7 = self.max(v6)
        v8 = self.relu(v7)
        v9 = v8.data
        v10 = v9.data.data
        v11 = self.conv2d_6(x1)
        v12 = v11.data
        v13 = self.conv2d_4(v12)
        v14 = self.conv_transpose(v13)
        v15 = v14.data
        v16 = self.min_value
        v17 = torch.clamp_min(v15, v16)
        v18 = v17.data
        v19 = v18.data.data
        v20 = self.conv2d_10(x1)
        v21 = v20.data
        v22 = self.max(v21)
        v23 = self.relu(v22)
        v24 = v23.data
        v25 = v24.data.data
        v26 = self.conv2d_6(v25)
        v27 = self.conv2d_4(v26)
        v28 = v27.data
        v29 = self.conv_transpose(v28)
        v30 = v29.data
        v31 = self.min_value
        v32 = torch.clamp_min(v30, v31)
        v33 = v32.data
        v34 = v33.data.data
        v35 = self.conv2d_6(x1)
        v36 = self.conv2d_4(v35)
        v37 = v36.data
        v38 = self.conv_transpose(v37)
        v39 = v38.data
        v40 = self.max_value
        v41 = torch.clamp_max(v39, v40)
        v42 = v41.data
        v43 = v42.data.data
        v44 = self.conv2d_6(v35)
        v45 = self.conv2d_4(v44)
        v46 = self.conv_transpose(v45)
        v47 = v46.data
        v48 = self.min_value
        v49 = torch.clamp_min(v47, v48)
        v50 = v49.data
        v51 = v50.data.data
        v52 = torch.addmm(v19, v51, v25)
        v53 = v52.data
        v54 = self.max_value
        v55 = torch.clamp_max(v53, v54)
        v56 = v55.data
        v57 = v56.data.data
        v58 = self.conv2d_4(x1)
        v59 = v58.data
        v60 = v59.data.data
        v61 = self.conv_transpose(v60)
        v62 = v61.data
        v63 = self.conv2d_4(v62)
        v64 = v63.data
        v65 = v64.data.data
        v66 = torch.mul(v65, v13)
        v67 = v66.data
        v68 = torch.pow(v67, v58)
        v69 = v68.data
        v70 = self.conv2d_6(v13)
        v71 = v70.data
        v72 = self.conv2d_4(v71)
        v73 = v72.data
        v74 = v73.data.data
        v75 = torch.addmm(v25, v74, v35)
        v76 = v75.data
        v77 = v76.data.data
        v78 = torch.mul(v77, v13)
        v79 = v78.data
        v80 = torch.pow(v79, v13)
        v81 = v80.data
        v82 = torch.addmm(v69, v81, v66)
        v83 = v82.data
        v84 = self.max_value
        v85 = torch.clamp_max(v83, v84)
        v86 = v85.data
        v87 = v86.data.data
        v88 = torch.addmm(v57, v87, v52)
        v89 = v88.data
        v90 = self.max_value
        v91 = torch.clamp_max(v89, v90)
        v92 = v91.data
        v93 = v92.data.data
        v94 = self.conv2d_4(v60)
        v95 = v94.data
        v96 = v95.data.data
        v97 = torch.mul(v96, v35)
        v98 = v97.data
        v99 = torch.pow(v98, v25)
        v100 = v99.data
        v101 = torch.addmm(v87, v100, v75)
        v102 = v101.data
        v103 = v102.data.data
        v104 = torch.mul(v103, v35)
        v105 = v104.data
        v106 = torch.pow(v105, v35)
        v107 = v106.data
        v108 = torch.addmm(v100, v107, v97)
        v109 = v108.data
        v110 = self.max_value
        v111 = torch.clamp_max(v109, v110)
        v112 = v111.data
        v113 = v112.data.data
        v114 = torch.addmm(v93, v113, v88)
        v115 = v114.data
        v116 = self.max_value
        v117 = torch.clamp_max(v115, v116)
        v118 = v117.data
        v119 = v118.data.data
        v120 = torch.exp(v119)
        v121 = v120.data
        v122 = self.conv2d_4(v62)
        v123 = v122.data
        v124 = v123.data.data
        v125 = torch.mul(v124, v58)
        v126 = v125.data
        v127 = torch.pow(v126, v25)
        v128 = v127.data
        v129 = torch.addmm(v103, v128, v125)
        v130 = v129.data
        v131 = torch.exp(v130)
        v132 = v131.data
        v133 = self.conv2d_6(v58)
        v134 = v133.data
        v135 = v134.data.data
        v136 = torch.mul(v135, v51)
        v137 = v136.data
        v138 = torch.pow(v137, v25)
        v139 = v138.data
        v140 = torch.addmm(v96, v139, v136)
        v141 = v140.data
        v142 = torch.exp(v141)
        v143 = v142.data
        v144 = v143.data.data
        v145 = torch.mul(v144, v52)
        v146 = v145.data
        v147 = torch.pow(v146, v35)
        v148 = v147.data
        v149 = v148.data.data
        v150 = torch.mul(v149, v108)
        v151 = v150.data
        v152 = v151.data.data
        v153 = torch.mul(v148, v108)
        v154 = v153.data
        v155 = v154.data.data
        v156 = torch.mul(v150, v65)
        v157 = torch.addmm(v151, v152, v155)
        v158 = v156.data
        v159 = v157.data.data
        v160 = torch.mul(v150, v108)
        return v68



func = Model().to('cpu')


x1 = torch.randn(1, 2048, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 16, 7, 7], expected input[1, 2048, 7, 7] to have 16 channels, but got 2048 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7349ead96ec0>(*(FakeTensor(..., size=(1, 2048, 7, 7)), Parameter(FakeTensor(..., size=(1, 16, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 16, 7, 7], expected input[1, 2048, 7, 7] to have 16 channels, but got 2048 channels instead

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''