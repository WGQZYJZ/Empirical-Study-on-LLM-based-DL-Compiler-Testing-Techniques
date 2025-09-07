if True:
    # if statement branch 1
    x0 = self.conv(x0)
    x1 = self.pool_conv(x1)
else:
    # else statement branch 2
    x0 = self.pool_conv(x0)
    x1 = self.pool_conv(x1)


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        # if statement branch 1
        x2 = self.conv(x0)
        x3 = self.pool_conv(x1)
 
        y = torch.cat((x2, x3), dim=1)
        return y


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        # if statement branch 1
        x2 = self.conv(x0)
        x3 = self.pool_conv(x1)
 
        y = torch.cat((x2, x3), dim=1)
 
        # else statement branch 4
        z = self.pool_conv(y)
 
        if True:
            # if statement branch 5
            w = self.fcn(z)
        return w


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = self.conv_0(x1)
        x3 = self.conv_1(x2)
        y  = torch.cat((x2, x3), dim=1)
        z  = self.pool_conv(y)
        w  = self.fcn_classifier(z)
        return w


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        if True:
            # if statement branch 1
            y = torch.cat((x2, x3), dim=1)
 
        else:
            # else statement branch 4
            z = self.pool_conv(y)
 
            if True:
                # if statement branch 5
                w = self.fcn(z)
