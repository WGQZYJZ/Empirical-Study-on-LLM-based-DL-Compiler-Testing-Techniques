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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=32, out_channels=56, kernel_size=1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(in_channels=56, out_channels=64, kernel_size=1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(in_channels=64, out_channels=52, kernel_size=1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(in_channels=52, out_channels=60, kernel_size=1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(in_channels=60, out_channels=10, kernel_size=1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(in_channels=10, out_channels=18, kernel_size=1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(in_channels=18, out_channels=30, kernel_size=1, stride=1, padding=0)
        self.conv9 = torch.nn.Conv2d(in_channels=30, out_channels=6, kernel_size=1, stride=1, padding=0)
        self.conv10 = torch.nn.Conv2d(in_channels=6, out_channels=17, kernel_size=1, stride=1, padding=0)
        self.conv11 = torch.nn.Conv2d(in_channels=17, out_channels=17, kernel_size=1, stride=1, padding=0)
        self.conv12 = torch.nn.Conv2d(in_channels=17, out_channels=65, kernel_size=1, stride=1, padding=0)
        self.conv13 = torch.nn.Conv2d(in_channels=65, out_channels=71, kernel_size=1, stride=1, padding=0)
        self.conv14 = torch.nn.Conv2d(in_channels=71, out_channels=22, kernel_size=1, stride=1, padding=(0, 1))
        self.conv15 = torch.nn.Conv2d(in_channels=22, out_channels=47, kernel_size=1, stride=1, padding=0)
        self.conv16 = torch.nn.Conv2d(in_channels=47, out_channels=32, kernel_size=1, stride=1, padding=0)
        self.conv17 = torch.nn.Conv2d(in_channels=32, out_channels=28, kernel_size=1, stride=1, padding=0)
        self.conv18 = torch.nn.Conv2d(in_channels=28, out_channels=33, kernel_size=1, stride=1, padding=0)
        self.conv19 = torch.nn.Conv2d(in_channels=33, out_channels=30, kernel_size=1, stride=1, padding=0)
        self.conv20 = torch.nn.Conv2d(in_channels=30, out_channels=37, kernel_size=1, stride=1, padding=0)
        self.conv21 = torch.nn.Conv2d(in_channels=37, out_channels=39, kernel_size=1, stride=1, padding=0)
        self.conv22 = torch.nn.Conv2d(in_channels=39, out_channels=87, kernel_size=1, stride=1, padding=0)
        self.conv23 = torch.nn.Conv2d(in_channels=87, out_channels=18, kernel_size=1, stride=1, padding=0)
        self.conv24 = torch.nn.Conv2d(in_channels=18, out_channels=24, kernel_size=1, stride=1, padding=0)
        self.conv25 = torch.nn.Conv2d(in_channels=24, out_channels=13, kernel_size=1, stride=1, padding=0)
        self.conv26 = torch.nn.Conv2d(in_channels=13, out_channels=39, kernel_size=1, stride=1, padding=0)
        self.conv27 = torch.nn.Conv2d(in_channels=39, out_channels=26, kernel_size=1, stride=1, padding=0)
        self.conv28 = torch.nn.Conv2d(in_channels=26, out_channels=12, kernel_size=1, stride=1, padding=0)
        self.conv29 = torch.nn.Conv2d(in_channels=12, out_channels=2, kernel_size=1, stride=1, padding=0)
        self.conv30 = torch.nn.Conv2d(in_channels=2, out_channels=2, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        v9 = self.conv5(v8)
        v10 = torch.relu(v9)
        v11 = self.conv6(v10)
        v12 = torch.relu(v11)
        v13 = self.conv7(v12)
        v14 = torch.relu(v13)
        v15 = self.conv8(v14)
        v16 = torch.relu(v15)
        v17 = self.conv9(v16)
        v18 = torch.relu(v17)
        v19 = self.conv10(v18)
        v20 = torch.relu(v19)
        v21 = self.conv11(v20)
        v22 = torch.relu(v21)
        v23 = self.conv12(v22)
        v24 = torch.relu(v23)
        v25 = self.conv13(v24)
        v26 = torch.relu(v25)
        v27 = self.conv14(v26)
        v28 = torch.relu(v27)
        v29 = self.conv15(v28)
        v30 = torch.relu(v29)
        v31 = self.conv16(v30)
        v32 = torch.relu(v31)
        v33 = self.conv17(v32)
        v34 = torch.relu(v33)
        v35 = self.conv18(v34)
        v36 = torch.relu(v35)
        v37 = self.conv19(v36)
        v38 = torch.relu(v37)
        v39 = self.conv20(v38)
        v40 = torch.relu(v39)
        v41 = self.conv21(v40)
        v42 = torch.sigmoid(v41)
        v43 = self.conv22(v42)
        v44 = torch.sigmoid(v43)
        v45 = self.conv23(v44)
        v46 = torch.sigmoid(v45)
        v47 = self.conv24(v46)
        v48 = torch.sigmoid(v47)
        v49 = self.conv25(v48)
        v50 = torch.sigmoid(v49)
        v51 = self.conv26(v50)
        v52 = torch.sigmoid(v51)
        v53 = self.conv27(v52)
        v54 = torch.sigmoid(v53)
        v55 = self.conv28(v54)
        v56 = torch.sigmoid(v55)
        v57 = self.conv29(v56)
        v58 = torch.sigmoid(v57)
        v59 = self.conv30(v58)
        v60 = torch.sigmoid(v59)
        return v60




func = Model().to('cuda')



x1 = torch.randn(1, 3, 26, 24)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpc5w3e296/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpc5w3e296', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpc5w3e296/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''