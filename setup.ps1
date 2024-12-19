Add-Type -AssemblyName System.Windows.Forms

# Buat form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Modal Box tes"
$form.Size = New-Object System.Drawing.Size(300, 200)
$form.StartPosition = "CenterScreen"

# Buat label
$label = New-Object System.Windows.Forms.Label
$label.Text = "Masukkan Nama:"
$label.Location = New-Object System.Drawing.Point(10, 20)
$label.Size = New-Object System.Drawing.Size(100, 20)
$form.Controls.Add($label)

# Buat inputan nama
$namaTextBox = New-Object System.Windows.Forms.TextBox
$namaTextBox.Location = New-Object System.Drawing.Point(10, 50)
$namaTextBox.Size = New-Object System.Drawing.Size(260, 20)
$form.Controls.Add($namaTextBox)

# Buat tombol submit
$submitButton = New-Object System.Windows.Forms.Button
$submitButton.Text = "Submit"
$submitButton.Location = New-Object System.Drawing.Point(100, 80)
$submitButton.Size = New-Object System.Drawing.Size(100, 25)
$form.Controls.Add($submitButton)

# Tambahkan event handler untuk tombol submit
$submitButton.Add_Click({
    $nama = $namaTextBox.Text
    if (-not [string]::IsNullOrEmpty($nama)) {
        # Lakukan aksi setelah submit, contohnya menampilkan nama
        [System.Windows.Forms.MessageBox]::Show("Halo, $nama!")
    }
})

# Tampilkan form
$form.ShowDialog()