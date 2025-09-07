self.conv[i]  = torch.nn.Conv2d(...) for i in range(4)] 
for l in range(3):
    out  = self.conv[l](x) + x
    x10  = self.bn[l](out) 
    x11  = F.relu6(x10) 
    x12  = F.max_pool2d(x11, kernel_size=(3, 3), stride=2, padding=1)
    out  = self.conv[4+ l](x12)
