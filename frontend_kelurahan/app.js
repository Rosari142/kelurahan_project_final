document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';
    const token = 'b8ae367dfc9fca9e6974c7f41debdd80d886aa6a';
    const wargaListContainer = document.getElementById('warga-list-container');
    const addForm = document.getElementById('add-warga-form');
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');

    function renderWarga(warga) {
        const wargaDiv = document.createElement('div');

        const nama = document.createElement('h3');
        nama.textContent = warga.nama_lengkap;

        const nik = document.createElement('p');
        nik.textContent = `NIK: ${warga.nik}`;

        const alamat = document.createElement('p');
        alamat.textContent = `Alamat: ${warga.alamat}`;

        const telepon = document.createElement('p');
        telepon.textContent = `No. Telepon: ${warga.no_telepon}`;

        const updateBtn = document.createElement('button');
        updateBtn.textContent = 'Update';
        updateBtn.onclick = () => updateWarga(warga);

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteWarga(warga.id);

        wargaDiv.appendChild(nama);
        wargaDiv.appendChild(nik);
        wargaDiv.appendChild(alamat);
        wargaDiv.appendChild(telepon);
        wargaDiv.appendChild(updateBtn);
        wargaDiv.appendChild(deleteBtn);

        return wargaDiv;
    }

    function loadWarga(query='') {
        let url = apiUrl;
        if(query) url += `?search=${query}`;

        fetch(url, {
            headers: { 'Authorization': `Token ${token}` }
        })
        .then(res => res.json())
        .then(data => {
            wargaListContainer.innerHTML = '';
            data.results.forEach(warga => {
                const wargaEl = renderWarga(warga);
                wargaListContainer.appendChild(wargaEl);
            });
        })
        .catch(err => {
            wargaListContainer.innerHTML = '<p>Gagal memuat data. Pastikan server backend berjalan.</p>';
            console.error(err);
            alert('Gagal memuat data warga.');
        });
    }

    // Tambah warga baru
    addForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const newWarga = {
            nik: document.getElementById('nik').value,
            nama_lengkap: document.getElementById('nama_lengkap').value,
            alamat: document.getElementById('alamat').value,
            no_telepon: document.getElementById('no_telepon').value
        };

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify(newWarga)
        })
        .then(res => {
            if(!res.ok) throw new Error('Gagal menambah warga');
            return res.json();
        })
        .then(() => {
            addForm.reset();
            loadWarga();
            alert('Warga berhasil ditambahkan!');
        })
        .catch(err => {
            console.error(err);
            alert('Gagal menambah warga.');
        });
    });

    // Delete warga
    function deleteWarga(id) {
        if(!confirm('Apakah Anda yakin ingin menghapus warga ini?')) return;

        fetch(`${apiUrl}${id}/`, {
            method: 'DELETE',
            headers: { 'Authorization': `Token ${token}` }
        })
        .then(res => {
            if(res.status === 204) {
                loadWarga();
                alert('Warga berhasil dihapus!');
            } else throw new Error('Gagal menghapus warga');
        })
        .catch(err => {
            console.error(err);
            alert('Gagal menghapus warga.');
        });
    }

    // Update warga
    function updateWarga(warga) {
        const newName = prompt('Nama lengkap:', warga.nama_lengkap);
        if(!newName) return;

        fetch(`${apiUrl}${warga.id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify({
                nik: warga.nik,
                nama_lengkap: newName,
                alamat: warga.alamat,
                no_telepon: warga.no_telepon
            })
        })
        .then(res => {
            if(!res.ok) throw new Error('Gagal mengupdate warga');
            return res.json();
        })
        .then(() => {
            loadWarga();
            alert('Warga berhasil diupdate!');
        })
        .catch(err => {
            console.error(err);
            alert('Gagal mengupdate warga.');
        });
    }

    // Search warga
    searchButton.addEventListener('click', () => {
        const query = searchInput.value.trim();
        loadWarga(query);
    });

    // Load awal
    loadWarga();
});
