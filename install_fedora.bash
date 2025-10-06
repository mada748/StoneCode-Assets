echo "Downloading Repository"
git clone https://github.com/mada748/MinimalBrowser
cd MinimalBrowser
echo "Installing Required Dependices"
sudo dnf install python3
pip install PyQt5
pip install PyQtWebEngine
curl -s https://stonecode-assets.netlify.app/run.bash
echo "Dependices installed"
echo "Starting fedora.bash"
echo "I I     I I   EEEEE"
echo "I I I I I I   E   E"
echo "I I I I I I   E E E"
echo "I I     I I   EEEEE"
echo "I I     I I   E   E"
echo "I I     I I   E E E"
echo "I I     I I   EEEEE"
echo ""
echo ""
echo ""
echo "if you want to only run the browser file do: bash run.bash"
python3 browser.py
