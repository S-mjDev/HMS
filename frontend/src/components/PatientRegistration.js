import React, { useState, useEffect } from 'react';

function PatientRegistration() {
  const [formData, setFormData] = useState({
    firstname: '',
    midname: '',
    lastname: '',
    address: '',
    birthday: '',
    age: '',
    consultation_date: '',
    doctor: '',
    medical_history: ''
  });
  const [doctors, setDoctors] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Fetch doctors for the dropdown
    fetch('http://localhost:8000/doctor/')
      .then(response => response.json())
      .then(data => {
        // DRF returns {results: [...]} for paginated responses
        setDoctors(data.results || data || []);
      })
      .catch(error => console.error('Error fetching doctors:', error));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage('');

    // Prepare form data, converting doctor ID to URL if selected
    const submitData = {
      ...formData,
      doctor: formData.doctor ? `http://localhost:8000/doctor/${formData.doctor}/` : null
    };

    try {
      const response = await fetch('http://localhost:8000/patient/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(submitData)
      });

      if (response.ok) {
        setMessage('Patient registered successfully!');
        setFormData({
          firstname: '',
          midname: '',
          lastname: '',
          address: '',
          birthday: '',
          age: '',
          consultation_date: '',
          doctor: '',
          medical_history: ''
        });
      } else {
        const errorData = await response.json();
        setMessage('Error registering patient: ' + JSON.stringify(errorData));
      }
    } catch (error) {
      setMessage('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h2>Patient Registration</h2>
      {message && <p style={{ color: message.includes('Error') ? 'red' : 'green' }}>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label>First Name:</label>
          <input
            type="text"
            name="firstname"
            value={formData.firstname}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Middle Name:</label>
          <input
            type="text"
            name="midname"
            value={formData.midname}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Last Name:</label>
          <input
            type="text"
            name="lastname"
            value={formData.lastname}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Address:</label>
          <input
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Birthday:</label>
          <input
            type="date"
            name="birthday"
            value={formData.birthday}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Age:</label>
          <input
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Consultation Date:</label>
          <input
            type="date"
            name="consultation_date"
            value={formData.consultation_date}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Doctor:</label>
          <select
            name="doctor"
            value={formData.doctor}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          >
            <option value="">Select a doctor</option>
            {doctors.map(doctor => (
              <option key={doctor.id} value={doctor.id}>
                {doctor.firstname} {doctor.midname} {doctor.lastname} - {doctor.specialization}
              </option>
            ))}
          </select>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>Medical History:</label>
          <textarea
            name="medical_history"
            value={formData.medical_history}
            onChange={handleChange}
            rows="4"
            style={{ width: '100%', padding: '8px' }}
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          style={{
            padding: '10px 20px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            cursor: loading ? 'not-allowed' : 'pointer'
          }}
        >
          {loading ? 'Registering...' : 'Register Patient'}
        </button>
      </form>
    </div>
  );
}

export default PatientRegistration;