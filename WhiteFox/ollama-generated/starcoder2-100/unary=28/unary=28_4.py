

import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self._conv1 = nn.Conv2d(3, 8, kernel_size=7)
        self._conv2 = nn.Conv2d(8, 4, kernel_size=5)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = nn.functional.relu(x)
        y = self._conv1(x)
        y = nn.functional.relu(y)
        y = self._conv2(y)

        y = torch.clamp_max(
            nn.functional.relu(
                nn.functional.relu(
                    nn.functional.relu(
                        nn.functional.relu(
                            y, max=torch.tensor([0], dtype=float)) * -1.,
                        max=-2,
                    ),
                    max=-3),
                max=-4.),
        )
        y = torch.clamp_max(
            nn.functional.relu(nn.functional.relu(y)), max=-5.)

        return torch.softmax(y + x + 0.789)


