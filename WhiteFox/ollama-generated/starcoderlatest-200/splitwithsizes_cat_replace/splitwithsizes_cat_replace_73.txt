
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t = torch.split(x1, 3, dim=2)
        v1 = self._conv_block1(t[0]) + self._conv_block2(t[1]) + self._conv_block3(t[2]) # Concatenate all split tensors along dimension=2
        return torch.cat([v1], dim=2)
 
    def _conv_block1(self, t):
        v = torch.split(t, 1, dim=3) # Split all input channels into different tensors with shape=(64, H, W), where H and W are both equal to 8 
        v = self._conv1x1(v[0]) + self._conv3x3_reduce(v[1]) + self._conv3x3_expand(v[2]) # Concatenate all the split tensors along dimension=3
        return torch.cat([v], dim=3)
 
    def _conv_block2(self, t):
        v = torch.split(t, 4, dim=3) # Split all input channels into different tensors with shape=(H//2, H//2, W), where H and W are both equal to 16 
        v = self._conv1x1(v[0]) + self._conv3x3_reduce(v[1]) + self._conv3x3_expand(v[2]) # Concatenate all the split tensors along dimension=3
        return torch.cat([v], dim=3)
 
    def _conv_block3(self, t):
        v = torch.split(t, 8, dim=3) # Split all input channels into different tensors with shape=(H//4, H//4, W), where H and W are both equal to 16 
        v = self._conv1x1(v[0]) + self._conv3x3_reduce(v[1]) + self._conv3x3_expand(v[2]) # Concatenate all the split tensors along dimension=3
        return torch.cat([v], dim=3)
 
    def _conv1x1(self, t):
        v = F.relu(self._conv1x1_w1(t)) + self._conv1x1_b1(t) # Apply the ReLU activation to the output of 1x1 convolution with kernel size (1, 1), stride=1 and padding=0, plus the bias
        v = torch.nn.functional.adaptive_avg_pool2d(v, 8) # Pool the output of the above layer by (4, 4) to a tensor with shape=(H//4, W//4, channels/4)
        return v
 
    def _conv3x3_reduce(self, t):
        v = F.relu(self._conv3x3_reduce_w1(t)) + self._conv3x3_reduce_b1(t) # Apply the ReLU activation to the output of 3x3 convolution with kernel size (1, 1), stride=1 and padding=0, plus the bias
        return v
 
    def _conv3x3_expand(self, t):
        v = F.relu(self._conv3x3_expand_w1(t)) + self._conv3x3_expand_b1(t) # Apply the ReLU activation to the output of 3x3 convolution with kernel size (8, 8), stride=2 and padding=0, plus the bias
        return v
 
    def _conv1x1_w1(self, t):
        v = torch.nn.Conv2d(3, self._conv1x1_w1_outc, kernel_size=(1, 1)) # Apply 1x1 convolution with kernel size (1, 1), stride=1 and padding=0 to the input tensor
        v.load_state_dict(torch.nn.init.kaiming_normal_(v.weight))
        return v
 
    def _conv3x3_reduce_w1(self, t):
        v = torch.nn.Conv2d(self._conv3x3_reduce_w1_inc, self._conv3x3_reduce_w1_outc, kernel_size=(1, 1)) # Apply 3x3 convolution with kernel size (1, 1), stride=1 and padding=0 to the output of _conv1x1
        v.load_state_dict(torch.nn.init.kaiming_normal_(v.weight))
        return v
 
    def _conv3x3_expand_w1(self, t):
        v = torch.nn.Conv2d(3, self._conv3x3_expand_w1_outc, kernel_size=(8, 8), stride=2) # Apply 3x3 convolution with kernel size (8, 8), stride=2 and padding=0 to the input tensor
        v.load_state_dict(torch.nn.init.kaiming_normal_(v.weight))
        return v
 
    def _conv1x1_b1(self, t):
        v = torch.nn.Conv2d(3, 3, kernel_size=(1, 1), stride=1) # Apply 1x640004,40:3,6)
     
     
