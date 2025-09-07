    t1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0) 
    t2 = torch.nn.Conv2d(3, 9, 1, stride=1, padding=0)
    conv_out = t1(x1) + t2(x1)
    act_out  = F.relu(conv_out)
