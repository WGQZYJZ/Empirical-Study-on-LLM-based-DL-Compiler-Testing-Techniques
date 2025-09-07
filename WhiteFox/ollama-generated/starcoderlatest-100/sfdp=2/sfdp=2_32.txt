
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
    
    def forward(self, x1, x2):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output


# Test Codes
class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2  = torch.erf(x1) # Apply the error function to the input tensor
        t3  = t2 * 0.5 # Multiply the output of the error function by 0.5
        t4  = t2 * 0.7071067811865476 # Multiply the output of the error function by 0.7071067811865476
        t5  = t3 + 1 # Add 1 to the output of the addition operation
        t6  = t4 * t5 # Multiply the output of the addition operation by the output of the multiplication operation
        return torch.nn.functional.avg_pool2d(t6, 3, stride=2)


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(80, 192, kernel_size=(3,3), padding=(0,0))
        self.conv2 = torch.nn.Conv2d(192, 192, kernel_size=(4,4), stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = F.avg_pool2d(v1, (2,2))
        v3 = self.conv2(v2)
        return v3


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(80, 192, kernel_size=(3,3), padding=(0,0))
        self.conv2 = torch.nn.Conv2d(192, 576, kernel_size=(4,4), stride=2, padding=1)
 
    def forward(self, x):
        v1 = F.interpolate(x, scale_factor=0.5, mode='bilinear')
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        return v3


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn1 = torch.nn.BatchNorm2d(64, affine=True) # apply BN to the input tensor before the convolution
        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=(3,3), padding=(1,1))
 
    def forward(self, x):
        v1 = self.bn1(x) # Apply BN before the first convolution layer
        v2 = self.conv1(v1) # Convolve with kernel size (3,3) and stride 1 to the output of the batch norm layer
        return v2


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(80, 192, kernel_size=(3,3), padding=(0,0))

    def forward(self, x):
        v1 = F.interpolate(x, scale_factor=0.5, mode='bilinear')
        v2 = self.conv1(v1)
        return v2


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn1 = torch.nn.BatchNorm2d(64, affine=True) # apply BN to the input tensor before the convolution
        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=(3,3), padding=(1,1))

    def forward(self, x):
        v1 = self.bn1(x) # Apply BN before the first convolution layer
        v2 = self.conv1(v1) # Convolve with kernel size (3,3) and stride 1 to the output of the batch norm layer
        return v2


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bn1 = torch.nn.BatchNorm2d(64, affine=True) # apply BN to the input tensor before the convolution
        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=(3,3), padding=(1,1))

    def __init__(self):
        
       
        
# +
if ( ( True or True) ) ):
    # print print print print print print print print 
    if True:
        # 
        # 
        pass
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #                                                                       
        
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =