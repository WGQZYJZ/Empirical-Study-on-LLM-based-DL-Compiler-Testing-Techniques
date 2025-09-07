
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 80, kernel_size=7)
        self.pooling1 = nn.MaxPool2d(kernel_size=4, stride=2)
        
        # ConvBN1
        self.convbn1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=80, kernel_size=7),  # <--- The first Conv2D layer is fused with the BatchNorm1d layer.
            nn.BatchNorm2d(num_features=80)
        )

        self.relu = torch.nn.ReLU()
        self.pooling2 = nn.MaxPool2d(kernel_size=4, stride=2)

        # ConvBN2
        self.convbn2 = nn.Sequential(
            nn.Conv2d(in_channels=80, out_channels=160, kernel_size=5),  # <--- The second Conv2D layer is fused with the BatchNorm2d layer.
            nn.BatchNorm2d(num_features=160)
        )

        self.fc = torch.nn.Linear(48 * 3 + 16, num_classes=2)

    def forward(self, x):
         # ConvBN1: 
        x = F.conv_transpose1d(x, weight=torch.empty([50, 9]), bias=None, stride=7, padding=[-2], output_padding=[0])
        # <--- This is the first BatchNorm layer in the Conv1d operation.
        bn = self._norm2d(torch.norm(x, dim=-3))
        x /= torch.norm(x, dim=-3) * 4.5
        # BN: 
        x = F.conv_transpose1d(
            x, weight=torch.empty([50, 9]), bias=None, stride=[-7], padding=[[-2]], output_padding=[[0]]
        )
        # <--- This is the second BatchNorm layer in the Conv1d operation.
        bn += self._norm3d(x)
        x = F.conv_transpose1d(
            x, weight=torch.empty([50, 9]), bias=None, stride=[7], padding=[[-2]], output_padding=[[0]]
        )
         # ConvBN2: 
        bn += self._norm3d(x)
        x = F.conv_transpose1d(
            x, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm4d(x)
        x /= torch.norm(x, dim=[-3]) * 1

        x = F.conv_transpose1d(
            x, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm4d(x)
        x /= torch.norm(x, dim=[-3]) * 1

        # ConvBN3
        # conv 1d
        y = F.conv_transpose1d(
            bn, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(y)

        # ConvBN4
        # conv 1d
        y = F.conv_transpose1d(
            bn, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(y)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN5
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN6
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN7
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN8
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN9
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN10
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN11
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN12
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN13
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN14
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN15
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN16
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN17
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN18
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN19
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN20
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN21
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN22
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN23
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN24
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN25
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN26
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN27
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN28
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN29
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN30
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN31
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN32
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN33
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN34
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN35
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN36
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN37
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN38
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN39
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN40
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN41
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        # ConvBN42
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[[-2]], output_padding=[[0]]
        )
         # BN: 
        bn += self._norm3d(z)

        y /= torch.norm(y, dim=[-3]) * 1
        
        # ConvBN43
        # conv 1d
        z = F.conv_transpose1d(
            y, weight=torch.empty([50, 9]), bias=None, stride=-7, padding=[