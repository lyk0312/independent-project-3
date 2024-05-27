# Independent-project
## Fine-Tuning of Qwen-VL

1. `Qwen-VL.zip` is the package of Qwen-VL model after fine-tuning. The original file is download by https://github.com/QwenLM/Qwen-VL.git.
2. `dataset.ipynb` is the code for how to load the Rico dataset and align it to the fine-tuned format required by Qwen-VL.
3. `qwen-fine-turning.ipynb` is how to fine-tune the Qwen-VL. The detail of how it works can be seen in [Qwen-VL/README_CN.md at master · QwenLM/Qwen-VL (github.com)](https://github.com/QwenLM/Qwen-VL/blob/master/README_CN.md). After fine-tuning, the parameters are saved in "/Qwen-VL/output_qwen_chat/checkpoint-x" file.
4. `qwen-rico.ipynb` is to run the fine-tuned Qwen-VL and compare it with the original Qwen-VL. The parameters  saved in  "/Qwen-VL/output_qwen_chat/checkpoint-x" file can be chosen.

## MobileAgent via Qwen-VL

1. `MobileAgent-qwen.zip`is the package of MobileAgent via Qwen-VL. The The original file is download by https://github.com/X-PLUG/MobileAgent.git. The detail of MobileAgent can be seen in [X-PLUG/MobileAgent: Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception (github.com)](https://github.com/X-PLUG/MobileAgent/tree/main)

2. To run MobileAgent-qwen, please refer to [MobileAgent/MobileAgent-qwen/README.md at main · X-PLUG/MobileAgent (github.com)](https://github.com/X-PLUG/MobileAgent/blob/main/MobileAgent-qwen/README.md). The `run_xxx.py` files are cases for testing the performance of MobileAgent via Qwen-VL.
