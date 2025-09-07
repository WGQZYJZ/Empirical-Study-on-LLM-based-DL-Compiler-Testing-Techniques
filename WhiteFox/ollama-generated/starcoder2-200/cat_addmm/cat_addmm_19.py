
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, kernel_size=1)
        
        self.linear0 = torch.nn.Linear(in_features=64*dim**2*8, out_features=int(512/dim))
        self.bn0 = torch.nn.BatchNorm1d(num_features=self.linear0.out_features)
 
        self.relu  = torch.nn.ReLU()
 
        self.dropout = torch.nn.Dropout()
        
        self.fc3 = torch.nn.Linear(in_features=512, out_features=dim**4*8)
        self.bn6 = torch.nn.BatchNorm1d(num_features=self.fc3.out_features)
 
        self.convT  = torch.nn.ConvTranspose2d(in_channels=dim**4*8, out_channels=int((dim/8)**2), kernel_size=5, stride=2)
        self.conv4  = torch.nn.Conv2d(in_channels=int((dim/8)**2)*100, out_channels=3, kernel_size=7, stride=2)
 
    def forward(self, x):
        
        # Block 1
        v1 = self.conv(x)
        v2 = self.relu(v1)
        v5 = torch.addmm(v2, mat1, mat2)
        
        # Block 2
        v7  = torch.cat([v3], dim=dim)
        v8 = v4  +  1
        v9  = v0.permute(3,2,1,0) * v6 * v5
        v10 = self.relu(self.bn0(v9))
        v11 = self.linear(v10).reshape(x[:, :4],x[:, 4:])
        v12 = self.conv(v8)
        
        # Block 3
        v16 = torch.addmm(x, mat1, mat2)
        v17 = v5 +  1
        
        # The final output
        v20 = self.dropout(self.bn6(v14))
        v21 = v9.permute(3, 2, 0).reshape(-1,) * (v8 * v17 + x)
        return torch.erf(self.convT(v11)) + v15 * v20 * v16 * v2


# Initializing the model