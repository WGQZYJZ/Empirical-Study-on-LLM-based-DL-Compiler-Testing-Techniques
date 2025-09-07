
import torch  # type: ignore
import math 

class Model(torch.nn.Module):
    def __init__(self, num_heads=8) -> None:
        super().__init__()

        self.num_heads = num_heads
        
        self.key1 = torch.nn.Conv2d(3, 64, kernel_size=[7] * 3)
        self.key2 = torch.nn.Conv2d(8*self.num_heads, 1024//self.num_heads, groups=self.num_heads)
        self.query1 = torch.nn.Linear(65536, 1024)
        self.query2 = torch.nn.Linear(8 * self.num_heads*8 * 1024//self.num_heads, num_features=8)
        self.value1 = torch.nn.Conv2d(3, 64, kernel_size=[7] * 3)
        self.value2 = torch.nn.Conv2d(8*self.num_heads, 500//self.num_heads, groups=self.num_heads)


    def forward(self, x1):

        # Compute the dot product of the query and key
        k1 = self.key1(x1).transpose(-2,-3).contiguous()
        k2 = self.key2(k1.permute([0, 3, 4,5]).reshape((
            -1,8*self.num_heads,
            56//self.num_heads,
            7*3-7//self.num_heads
        ))).contiguous()
        query = self.query2(k2.permute([0,3,4,-1])).flatten(-2) # (N, num_head, 8 * 8) * 512 * 8 * 8 * 64 -> N * 8 * 512 -> N * 512
        query = self.query1(query).reshape((x1.size(-3), x1.size(-2), x1.size(-1), 1024))

        # Compute the dot product of the attention weights and the value tensor
        v1 = self.value1(x1)
        v2 = self.value2(v1.permute([0,3,-1,4]))
        return torch.matmul(query, v2)


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn((8,8,65536))

 __output__= m(x1)
