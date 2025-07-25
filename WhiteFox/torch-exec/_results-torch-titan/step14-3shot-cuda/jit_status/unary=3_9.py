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

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=4)
        self.conv2 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=12)
        self.conv3 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=18)
        self.conv5 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=5)
        self.conv6 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=20)
        self.conv7 = torch.nn.Conv2d(32, 64, 1, stride=1, padding=4)
        self.conv8 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=19)
        self.conv9 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=20)
        self.conv10 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=15)
        self.conv11 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=11)
        self.conv12 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=12)
        self.conv13 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=16)
        self.conv14 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=13)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        v14 = (v13 * 0.5)
        v15 = (v13 * 0.7071067811865476)
        v16 = torch.erf(v15)
        v17 = (v16 + 1)
        v18 = (v14 * v17)
        v19 = self.conv4(v18)
        v20 = (v19 * 0.5)
        v21 = (v19 * 0.7071067811865476)
        v22 = torch.erf(v21)
        v23 = (v22 + 1)
        v24 = (v20 * v23)
        v25 = self.conv5(v24)
        v26 = (v25 * 0.5)
        v27 = (v25 * 0.7071067811865476)
        v28 = torch.erf(v27)
        v29 = (v28 + 1)
        v30 = (v26 * v29)
        v31 = self.conv6(v30)
        v32 = (v31 * 0.5)
        v33 = (v31 * 0.7071067811865476)
        v34 = torch.erf(v33)
        v35 = (v34 + 1)
        v36 = (v32 * v35)
        v37 = self.conv7(v36)
        v38 = (v37 * 0.5)
        v39 = (v37 * 0.7071067811865476)
        v40 = torch.erf(v39)
        v41 = (v40 + 1)
        v42 = (v38 * v41)
        v43 = self.conv8(v42)
        v44 = (v43 * 0.5)
        v45 = (v43 * 0.7071067811865476)
        v46 = torch.erf(v45)
        v47 = (v46 + 1)
        v48 = (v44 * v47)
        v49 = self.conv9(v48)
        v50 = (v49 * 0.5)
        v51 = (v49 * 0.7071067811865476)
        v52 = torch.erf(v51)
        v53 = (v52 + 1)
        v54 = (v50 * v53)
        v55 = self.conv10(v54)
        v56 = (v55 * 0.5)
        v57 = (v55 * 0.7071067811865476)
        v58 = torch.erf(v57)
        v59 = (v58 + 1)
        v60 = (v56 * v59)
        v61 = self.conv11(v60)
        v62 = (v61 * 0.5)
        v63 = (v61 * 0.7071067811865476)
        v64 = torch.erf(v63)
        v65 = (v64 + 1)
        v66 = (v62 * v65)
        v67 = self.conv12(v66)
        v68 = (v67 * 0.5)
        v69 = (v67 * 0.7071067811865476)
        v70 = torch.erf(v69)
        v71 = (v70 + 1)
        v72 = (v68 * v71)
        v73 = self.conv13(v72)
        v74 = (v73 * 0.5)
        v75 = (v73 * 0.7071067811865476)
        v76 = torch.erf(v75)
        v77 = (v76 + 1)
        v78 = (v74 * v77)
        v79 = self.conv14(v78)
        return v79




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpj_cpf9z4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpj_cpf9z4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpj_cpf9z4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''