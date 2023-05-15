from pathlib import Path, PurePath
import os
from datetime import datetime, timedelta

# ====================== DIRETÓRIOS LOCAIS e DATAS ======================
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
DATA_DIRECTORY = os.path.join(ROOT, "Data")
NOW = datetime.now().strftime("%d/%m %H:%M")
CURRENT_DAY = datetime.now().strftime("%d/%m")
# ===============================================================
