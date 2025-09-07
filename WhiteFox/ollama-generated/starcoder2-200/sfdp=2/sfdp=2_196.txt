
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Query
        self.linear1 = torch.nn.Linear(5, 7)
        self.batchnorm1 = torch.nn.BatchNorm2d(4096)
        self.dropout1 = torch.nn.Dropout(0.3)
        self.layernorm1 = torch.nn.LayerNorm(normalized_shape=[-1])
 
        # Key
        self.linear2 = torch.nn.Linear(5, 7)
        self.batchnorm2 = torch.nn.BatchNorm2d(4096)
        self.dropout2 = torch.nn.Dropout(0.3)
        self.layernorm2 = torch.nn.LayerNorm(normalized_shape=[-1])
 
        # Value
        self.linear3 = torch.nn.Linear(5, 7)
        self.batchnorm3 = torch.nn.BatchNorm2d(4096)
        self.dropout3 = torch.nn.Dropout(0.3)
        self.layernorm3 = torch.nn.LayerNorm(normalized_shape=[-1])
 
    def forward(self, query):
        k1  = self.linear1(query) 
        k2  = self.batchnorm1(k1 + k1.div(inv_scale_factor))  
        k3  = self.dropout1(k2)
        k4  = self.layernorm1(k3, eps=1e-5)
 
        k1  = self.linear2(query) 
        k2  = self.batchnorm2(k1 + k1.div(inv_scale_factor))  
        k3  = self.dropout2(k2)
        k4  = self.layernorm2(k3, eps=1e-5)
 
        k1  = self.linear3(query) 
        k2  = self.batchnorm3(k1 + k1.div(inv_scale_factor))  
        k3  = self.dropout3(k2)
        k4  = self.layernorm3(k3, eps=1e-5)
 
        return k4
